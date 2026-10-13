# Security Policy

## Supported Versions

| Version | Supported |
| ------- | --------- |
| 0.4.x   | yes       |
| 0.3.x   | yes       |
| < 0.3   | no        |

## Reporting a Vulnerability

Email `security@forge-labs.dev` with:
- Affected version
- Reproduction steps
- Impact assessment

Do **not** open public issues for security bugs. We aim to respond within
72 hours and patch within 14 days for confirmed issues.

## Scope

- Prompt injection against the local LLM backend
- Path traversal in the batch importer
- Arbitrary file write via custom template loader
- DoS via unbounded generation requests

Out of scope: trademark disputes over generated names (that's on you,
check USPTO before you file).