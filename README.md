# GTFS Validator

Validate GTFS Schedule feeds with the [GTFS Analyzer](https://github.com/ttezer/gtfs-analyzer)
engine. Attach a GTFS ZIP, give a local path, or paste a public feed URL, and get a report on
whether the feed is publishable, its scores, and the fixes that matter most, in priority order.

## Use it

Type `/gtfs` and attach a feed, or ask in your own words, for example "Validate this GTFS
feed". You can also ask what a rule means, such as `/gtfs TRP_002`.

## Data

The analysis runs where Claude runs: in Claude's code sandbox on claude.ai, or on your own
computer in Claude Code. The plugin installs the open-source `gtfs-analyzer` package from PyPI
(pinned version) and, when you give a URL, downloads the feed from that URL. The feed is not
sent to any server operated by this plugin, and nothing is stored.

## License

MIT
