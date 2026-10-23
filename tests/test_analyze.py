"""Tests for skills/gtfs/scripts/analyze.py against the real gtfs-analyzer engine.

The demo feed in fixtures/demo-feed has deliberate faults: stop_times go backwards on
trip T1 (STM_008), and stop S4 duplicates S3's coordinates and serves no trip.
"""

from __future__ import annotations

import importlib.util
import io
import json
import subprocess
import sys
import zipfile
from pathlib import Path

import pytest

gtfs_analyzer = pytest.importorskip("gtfs_analyzer")

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "gtfs" / "scripts" / "analyze.py"
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "demo-feed"
TODAY = "20261015"


def build_zip(path: Path, drop: tuple[str, ...] = ()) -> Path:
    with zipfile.ZipFile(path, "w") as archive:
        for file in sorted(FIXTURE.glob("*.txt")):
            if file.name not in drop:
                archive.write(file, file.name)
    return path


def run(*args: str, python_flags: tuple[str, ...] = ()) -> tuple[int, dict]:
    proc = subprocess.run(
        [sys.executable, *python_flags, str(SCRIPT), *args],
        capture_output=True, text=True, check=False,
    )
    return proc.returncode, json.loads(proc.stdout)


@pytest.fixture
def feed(tmp_path: Path) -> Path:
    return build_zip(tmp_path / "feed.zip")


def test_complete_summary_keeps_engine_verdict_scores_and_order(feed: Path) -> None:
    code, out = run(str(feed), "--today", TODAY, "--max-priorities", "100")
    engine = gtfs_analyzer.validate_gtfs(str(feed), today=TODAY)

    assert code == 0
    assert out["validation_status"] == "COMPLETE"
    assert out["publishability"] == engine["reports"]["r1"]
    assert out["scores"] == engine["reports"]["r5"]
    assert [p["rule_id"] for p in out["r9_priorities"]] == [i["rule_id"] for i in engine["reports"]["r9"]["items"]]
    assert out["total_notices"] == len(engine["notices"])
    assert sum(out["severity_counts"].values()) == out["total_notices"]
    assert out["engine_version"] == gtfs_analyzer.__version__
    assert "metrics" in out and "file_stats" not in out["metrics"]


def test_known_faults_are_reported_with_examples(feed: Path) -> None:
    _, out = run(str(feed), "--today", TODAY, "--max-priorities", "100")
    by_rule = {p["rule_id"]: p for p in out["r9_priorities"]}

    assert "STM_008" in by_rule
    assert by_rule["STM_008"]["examples"][0]["file"] == "stop_times.txt"
    assert {"STP_016", "STP_020"} <= set(by_rule)
    assert {r["rule_id"] for r in out["rules"]} >= {"STM_008", "STP_016", "STP_020"}


def test_limits_cap_priorities_and_examples(feed: Path) -> None:
    _, out = run(str(feed), "--today", TODAY, "--max-priorities", "2", "--examples", "1")

    assert len(out["r9_priorities"]) == 2
    assert all(len(p["examples"]) <= 1 for p in out["r9_priorities"])
    assert out["r9_total"] > 2


def test_language_switches_notice_text(feed: Path) -> None:
    _, en = run(str(feed), "--today", TODAY, "--lang", "en")
    _, tr = run(str(feed), "--today", TODAY, "--lang", "tr")

    assert en["r9_priorities"][0]["rule_id"] == tr["r9_priorities"][0]["rule_id"]
    assert en["r9_priorities"][0]["title"] != tr["r9_priorities"][0]["title"]


def test_partial_result_is_marked_and_not_publishable(tmp_path: Path) -> None:
    feed = build_zip(tmp_path / "partial.zip", drop=("routes.txt",))
    code, out = run(str(feed), "--today", TODAY)

    assert code == 0
    assert out["validation_status"] == "PARTIAL"
    assert "routes.txt" in out["partial"]["unavailable_files"]
    assert out["publishability"]["publishable"] is False
    assert out["blocker_total"] == len(out["publishability"]["blocker_notice_ids"]) >= 1
    assert out["blockers"][0]["rule_id"]


def test_unreadable_zip_is_fatal(tmp_path: Path) -> None:
    bad = tmp_path / "bad.zip"
    bad.write_bytes(b"not a zip")
    code, out = run(str(bad))

    assert code == 2
    assert out["error"] == "FATAL"


@pytest.mark.parametrize("args", [
    ("missing.zip",),
    ("{feed}", "--today", "20261301"),
    ("{feed}", "--examples", "-1"),
    ("{feed}", "--lang", "de"),
    (),
])
def test_input_errors_use_exit_code_4(feed: Path, args: tuple[str, ...]) -> None:
    code, out = run(*(a.format(feed=feed) for a in args))

    assert code == 4
    assert out["error"] == "INPUT"


def test_missing_package_is_reported(feed: Path) -> None:
    # -S skips site-packages, so the engine cannot be imported.
    code, out = run(str(feed), python_flags=("-S",))

    assert code == 3
    assert out["error"] == "PACKAGE_MISSING"
    assert "gtfs-analyzer==" in out["message"]


@pytest.mark.parametrize("lang", ["en", "tr", "fr", "ja"])
def test_rule_lists_cover_rules_the_engine_reports(feed: Path, lang: str) -> None:
    rules_file = ROOT / "skills" / "gtfs" / "references" / f"rules.{lang}.md"
    text = rules_file.read_text(encoding="utf-8")
    _, out = run(str(feed), "--today", TODAY)

    missing = [r["rule_id"] for r in out["rules"] if f"| {r['rule_id']} |" not in text]
    assert not missing
    assert rules_file.stat().st_size < 256 * 1024


def test_version_mismatch_adds_warning(feed: Path, monkeypatch, capsys) -> None:
    spec = importlib.util.spec_from_file_location("analyze", SCRIPT)
    analyze = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(analyze)
    monkeypatch.setattr(gtfs_analyzer, "__version__", "0.0.0")
    monkeypatch.setattr(sys, "argv", ["analyze.py", str(feed), "--today", TODAY])

    with pytest.raises(SystemExit) as exit_info:
        analyze.main()

    out = json.loads(capsys.readouterr().out)
    assert exit_info.value.code == 0
    assert out["engine_version"] == "0.0.0"
    assert out["version_warning"] == f"expected gtfs-analyzer {analyze.PINNED_VERSION}"
