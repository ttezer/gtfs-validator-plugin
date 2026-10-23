# GTFS Validator

Validate GTFS Schedule feeds with the [GTFS Analyzer](https://github.com/ttezer/gtfs-analyzer)
engine. Attach a GTFS ZIP, give a local path, or paste a public feed URL, and get a report on
whether the feed is publishable, its scores, and the fixes that matter most, in priority order.

## Use it

Type `/gtfs` and attach a feed, or ask in your own words, for example "Validate this GTFS
feed". You can also ask what a rule means, such as `/gtfs TRP_002`.

The report gives:

- the publishability verdict and any blocking findings
- the overall, publishing, spec, interoperability, quality, and analytics scores
- the feed's size and service window
- the highest-priority fixes, each with the file, line, and values involved

Results come from the engine as they are: the plugin does not recompute scores or change the
verdict. Answers follow your language; rule texts are available in English, Turkish, French,
and Japanese.

## Requirements

- Code execution must be turned on in your settings, because the analysis runs as a script.
- A ready-made engine package exists for Linux x86_64, macOS on Apple silicon, and Windows
  x86_64. On other platforms, use the browser version at https://ttezer.github.io/gtfs-analyzer/,
  which runs the same engine on your device.
- In chat, the code sandbox cannot download feeds from URLs. Download the ZIP and attach it
  instead.

## Data

The analysis runs where Claude runs: in Claude's code sandbox on claude.ai, or on your own
computer in Claude Code. The plugin installs the open-source `gtfs-analyzer` package from PyPI
(pinned version) and, when you give a URL, downloads the feed from that URL. On your own
computer the package is installed into a separate environment at
`~/.cache/gtfs-validator/venv`. The feed is not sent to any server operated by this plugin, and
nothing is stored.

## Development

- `tests/`: script tests against a small fixture feed; run them with pytest in an environment
  where `gtfs-analyzer` is installed.
- `evals/`: behavior evals for the skill; the scaffold scripts build the test feeds and install
  the engine.

## License

MIT
