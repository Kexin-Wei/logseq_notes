# A03:2025 - Software Supply Chain Failures

Vulnerabilities introduced through compromised dependencies, libraries, or development tools.

## How It Works

- a) Dependency Confusion
	- Attackers upload malicious packages with same name to public repos
- b) Compromised Libraries
	- Popular packages get hijacked (event-stream, ua-parser-js)
- c) Outdated Dependencies
	- Using libraries with known CVEs
- d) Build Tool Compromise
	- SolarWinds-style attacks on CI/CD pipeline

## Real-World Examples

- **SolarWinds (2020)**: Build system compromise affected 18,000 customers
- **event-stream (2018)**: Popular npm package injected with Bitcoin stealer
- **Codecov (2021)**: Bash uploader script modified to exfiltrate environment variables
- **Log4Shell (2021)**: Widespread Log4j vulnerability in countless applications

## Defense

- Pin dependency versions
- Use private registries
- Regular dependency audits
- Software Bill of Materials (SBOM)
- Verify package integrity
