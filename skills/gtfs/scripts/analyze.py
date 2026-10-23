"""Validate a GTFS ZIP with the gtfs-analyzer package and print a compact JSON summary.

The engine result can hold hundreds of thousands of notices, so this script keeps the
engine's verdict, scores and R9 priority order as returned and adds only counts and a few
example notices per prioritized rule. It never recomputes scores or publishability.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter

PINNED_VERSION = "0.16.0"
LANGS = ("en", "tr", "fr", "ja")

EXAMPLE_FIELDS = ("file", "line", "field", "entity_id", "observed_value", "expected_value", "message")


def emit(payload: dict, code: int = 0) -> None:
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")
    sys.exit(code)


def notice_brief(notice: dict) -> dict:
    return {k: notice[k] for k in EXAMPLE_FIELDS if notice.get(k) is not None}


def summarize(result: dict, max_priorities: int, examples: int) -> dict:
    notices = result["notices"]
    by_id = {n["id"]: n for n in notices}
    reports = result["reports"]

    rules: dict[str, dict] = {}
    for n in notices:
        entry = rules.get(n["rule_id"])
        if entry is None:
            rules[n["rule_id"]] = {
                "rule_id": n["rule_id"],
                "severity": n["severity"],
                "rule_class": n["rule_class"],
                "title": n["title"],
                "count": 1,
            }
        else:
            entry["count"] += 1

    priorities = []
    for item in reports["r9"]["items"][:max_priorities]:
        ids = item.get("notice_ids", [])
        first = by_id.get(ids[0]) if ids else None
        priorities.append({
            "rule_id": item["rule_id"],
            "title": first["title"] if first else None,
            "severity": first["severity"] if first else None,
            "rule_class": first["rule_class"] if first else None,
            "labels": item.get("labels"),
            "priority_score": item.get("priority_score"),
            "score_delta": item.get("score_delta"),
            "pub_score_delta": item.get("pub_score_delta"),
            "affected_instance_count": item.get("affected_instance_count"),
            "fix_effort": item.get("fix_effort"),
            "remediation": first["remediation"] if first else None,
            "examples": [notice_brief(by_id[i]) for i in ids[:examples] if i in by_id],
        })

    blockers = [by_id[i] for i in reports["r1"].get("blocker_notice_ids", []) if i in by_id]
    metrics = {k: v for k, v in result["metrics"].items() if k != "file_stats"}

    summary = {
        "validation_status": result["validation_status"],
        "publishability": reports["r1"],
        "scores": reports["r5"],
        "metrics": metrics,
        "severity_counts": dict(Counter(n["severity"] for n in notices)),
        "total_notices": len(notices),
        "capped_totals": result.get("capped_totals") or {},
        "blockers": [dict(notice_brief(n), rule_id=n["rule_id"], title=n["title"]) for n in blockers[:examples * 4]],
        "blocker_total": len(blockers),
        "r9_priorities": priorities,
        "r9_total": len(reports["r9"]["items"]),
        "rules": sorted(rules.values(), key=lambda r: -r["count"]),
        "agency_count": (result.get("feed_summary") or {}).get("agency_count"),
    }
    if "partial" in result:
        summary["partial"] = result["partial"]
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("feed", help="path to a GTFS ZIP file")
    parser.add_argument("--lang", default="en", choices=LANGS)
    parser.add_argument("--today", help="validation date, YYYYMMDD (defaults to today)")
    parser.add_argument("--max-priorities", type=int, default=15)
    parser.add_argument("--examples", type=int, default=3)
    args = parser.parse_args()

    try:
        import gtfs_analyzer
    except ImportError:
        emit({
            "error": "PACKAGE_MISSING",
            "message": f"Install the engine first: pip install gtfs-analyzer=={PINNED_VERSION}",
        }, 3)

    kwargs = {"lang": args.lang}
    if args.today:
        kwargs["today"] = args.today
    try:
        result = gtfs_analyzer.validate_gtfs(args.feed, **kwargs)
    except gtfs_analyzer.ValidationError as err:
        emit({"error": "FATAL", "message": str(err), "engine_version": gtfs_analyzer.__version__}, 2)
    except (OSError, ValueError, TypeError) as err:
        emit({"error": "INPUT", "message": str(err)}, 2)

    summary = summarize(result, args.max_priorities, args.examples)
    summary["engine_version"] = gtfs_analyzer.__version__
    if gtfs_analyzer.__version__ != PINNED_VERSION:
        summary["version_warning"] = f"expected gtfs-analyzer {PINNED_VERSION}"
    emit(summary)


if __name__ == "__main__":
    main()
