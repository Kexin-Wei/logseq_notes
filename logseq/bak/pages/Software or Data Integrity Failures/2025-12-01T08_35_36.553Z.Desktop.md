# A08:2025 - Software or Data Integrity Failures

Failures to verify integrity of code, infrastructure, or data.

## How It Works

- a) Unsigned Code
	- No verification of package authenticity
- b) Insecure Deserialization
	- Untrusted data deserialized into objects
- c) Auto-Update Without Verification
	- Updates fetched over HTTP
	- No signature verification
- d) CI/CD Pipeline Compromise
	- Insecure build environments

## Real-World Examples

- **NotPetya (2017)**: Ukrainian accounting software update mechanism compromised
- **CCleaner (2017)**: Legitimate software update contained malware
- **ASUS (2019)**: Live Update tool compromised affecting 1M users
- **Java deserialization**: Numerous RCE vulnerabilities

## Defense

- Code signing
- Verify digital signatures
- Secure CI/CD pipeline
- Integrity checks (checksums, hashes)
- Avoid deserializing untrusted data
