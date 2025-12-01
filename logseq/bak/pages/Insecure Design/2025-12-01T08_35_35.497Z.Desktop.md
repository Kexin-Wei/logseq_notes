# A06:2025 - Insecure Design

Fundamental architectural flaws and missing security controls.

## How It Works

- a) Missing Rate Limiting
	- No protection against brute force
- b) Insecure Workflows
	- Password reset without identity verification
- c) Lack of Security Boundaries
	- No separation between sensitive/public data
- d) Missing Threat Modeling
	- Security not considered during design phase

## Real-World Examples

- **Twitter (2020)**: API allowed phone number enumeration of all users
- **Clubhouse (2021)**: No rate limiting allowed data scraping
- **Zoom (2020)**: Meeting IDs were sequential and predictable
- **Robinhood (2021)**: Social engineering due to insufficient verification

## Defense

- Implement threat modeling
- Rate limiting and throttling
- Secure by design principles
- Security requirements in SDLC
- Regular security architecture reviews
