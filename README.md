# BranchMark

**An MCP server that lets AI coding assistants query live CI test execution metrics and historical flakiness data directly from GitHub Actions.**

When AI coding assistants refactor code or fix bugs, they operate blind to how tests actually behave in CI, guessing whether a failure is a real regression or just transient infrastructure flakiness. BranchMark bridges this gap by exposing live workflow runs, job execution times, and historical test failure patterns directly through the Model Context Protocol. No more switching contexts to GitHub or guessing why CI failed.

## Example

<!-- A real command and its REAL pasted output. Run it first. -->

## Install

```bash
pip install -e ".[dev]"
```

## Usage

<!-- The 2-4 commands people actually need, one line each. -->

## How it works

- Queries GitHub Actions workflow runs via the GitHub REST API to fetch recent job and test execution data.
- Stores fetched run metadata in an in‑memory cache for quick access by the MCP server.
- Analyzes historical test outcomes to calculate a flakiness score for each test case.
- Exposes an MCP endpoint that returns live run details and flakiness metrics to AI assistants.
- Updates the cache periodically and on webhook triggers to keep data fresh.
- Emits JSON‑serialisable results that can be consumed by any client supporting the Model Context Protocol.

## Limitations

<!-- Honest and short: what it does NOT do, known gaps. -->

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
