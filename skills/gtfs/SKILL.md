---
name: gtfs
description: Validate a GTFS Schedule feed (a GTFS ZIP file, a local path, or a public feed URL) with the GTFS Analyzer engine and explain publishability, scores, and the highest-priority fixes. Use when the user asks to validate, check, or analyze a GTFS feed or transit timetable ZIP, or types /gtfs.
---

# GTFS Validator

Validate the feed with the GTFS Analyzer engine and explain its result. The engine is the
only source of findings: never invent notices, recompute scores, or override its verdict.

## 1. Get the feed

- An attached ZIP or a local path: use that file.
- A public URL: download it to a local file first (for example with `curl -fL -o feed.zip <url>`).
  If the download is blocked, ask the user to download the ZIP and attach it.
- Nothing given: ask for a GTFS ZIP or a public feed URL.

## 2. Make sure the engine is installed

Run `python3 -c "import gtfs_analyzer; print(gtfs_analyzer.__version__)"`. If that fails or
prints a version other than 0.16.0, install the pinned version:

```
pip install gtfs-analyzer==0.16.0
```

If pip refuses with "externally-managed-environment": in the chat's code sandbox, add
`--break-system-packages`; on the user's own computer, create a virtual environment instead
(`python3 -m venv ~/.cache/gtfs-validator/venv`) and use its `python`. If installation is
impossible (no network access to PyPI, or no wheel for this platform), tell the user and point
them to the browser version at https://ttezer.github.io/gtfs-analyzer/, which runs the same
engine on their device.

## 3. Run the analysis

```
python3 ${CLAUDE_SKILL_DIR}/scripts/analyze.py <feed.zip> --lang <en|tr|fr|ja>
```

If `${CLAUDE_SKILL_DIR}` is not replaced, use `scripts/analyze.py` relative to this file.
Pick `--lang` from the user's language; use `en` for any other language.

The script prints one JSON object. Exit code 2 with `"error": "FATAL"` means the engine could
not analyze the feed at all (for example an unreadable ZIP): report it as an analysis failure,
not as a verdict on the feed. Exit code 3 means the package is missing: go back to step 2.
Exit code 4 with `"error": "INPUT"` means a bad argument or an unreadable path: fix the call.

## 4. Explain the result

Report, in this order:

1. **Publishability**: `publishability.publishable` as returned. If it is false, list the
   `blockers`. Do not call a feed unpublishable because of other notices, and do not call it
   publishable when the engine says it is not.
2. **Scores**: `scores` (overall, pub, spec, interop, quality, analytics) exactly as returned.
3. **Feed at a glance**: stop, route, and trip counts and the service window from `metrics`.
4. **What to fix first**: `r9_priorities` in the given order. For each, give the rule ID, title,
   how many instances, the remediation, and one concrete example (file, line, values).
5. **Totals**: `severity_counts` and `total_notices`. ANALYTICS and QUALITY findings describe the
   feed; they do not make it invalid by themselves.

If `validation_status` is `PARTIAL`, say that coverage is incomplete and show `partial`. If
`version_warning` is present, mention which engine version produced the result.

## Rule questions

When the user asks what a rule ID means (for example `/gtfs TRP_002`), answer from the rule's
`title` and `remediation` in a result you already have. Otherwise describe it from
https://github.com/ttezer/gtfs-analyzer/blob/main/RULES.en.md and say where the text came from.
