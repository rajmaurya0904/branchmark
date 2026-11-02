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

<!-- 3-6 bullets: what it checks, computes or produces. -->

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
