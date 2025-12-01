# A04:2025 - Cryptographic Failures

Exposing sensitive data due to weak or missing encryption.

## How It Works

- a) Weak Algorithms
	- MD5, SHA1, DES still in use
- b) Unencrypted Transmission
	- HTTP instead of HTTPS
	- Cleartext protocols (FTP, Telnet)
- c) Poor Key Management
	- Hardcoded keys in source code
	- Predictable encryption keys
- d) Insufficient Randomness
	- Weak random number generators

## Real-World Examples

- **Adobe (2013)**: 153M passwords encrypted (not hashed) with same key
- **LinkedIn (2012)**: Passwords hashed without salt
- **Heartbleed (2014)**: OpenSSL vulnerability leaked memory contents
- **British Airways (2018)**: Credit card data transmitted over HTTP

## Defense

- Use modern encryption (AES-256, RSA-2048+)
- Enforce HTTPS everywhere
- Proper key management (rotate, separate)
- Salt and hash passwords (bcrypt, Argon2)
- Use proven crypto libraries
