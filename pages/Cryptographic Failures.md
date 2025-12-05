- Exposing sensitive data due to weak or missing encryption.
- ## How It Works
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
- ## Real-World Examples
	- **Adobe (2013)**: 153M passwords encrypted (not hashed) with same key
	- **LinkedIn (2012)**: Passwords hashed without salt
	- **Heartbleed (2014)**: OpenSSL vulnerability leaked memory contents
	- **British Airways (2018)**: Credit card data transmitted over HTTP
- ## Phase 1: TLS/SSL Analysis
	- **Certificate Check**
		- ```bash
		  openssl s_client -connect target.com:443 -servername target.com
		  echo | openssl s_client -connect target.com:443 2>/dev/null | openssl x509 -noout -dates
		  ```
	- **SSL/TLS Configuration**
		- ```bash
		  sslscan target.com
		  testssl.sh target.com
		  nmap --script ssl-enum-ciphers -p 443 target.com
		  ```
	- **Look for:**
		- SSLv2, SSLv3, TLS 1.0, TLS 1.1 (deprecated)
		- Weak ciphers (DES, RC4, export ciphers)
		- Missing HSTS header
		- Self-signed or expired certificates
- ## Phase 2: Protocol Analysis
	- **Cleartext Transmission**
		- ```bash
		  curl -I http://target.com
		  tcpdump -i eth0 -A port 80
		  ```
	- **Check for:**
		- Login forms over HTTP
		- API calls without TLS
		- Mixed content (HTTPS page loading HTTP resources)
		- Cleartext protocols: FTP (21), Telnet (23), SMTP (25)
- ## Phase 3: Cryptographic Implementation
	- **Password Storage**
		- Test password reset - does it send plaintext password?
		- Check if passwords appear in logs/responses
	- **Token Analysis**
		- ```bash
		  echo "token" | base64 -d
		  # Check JWT for "alg": "none" vulnerability
		  ```
	- **Encryption Weaknesses**
		- ECB mode detection (identical ciphertext blocks)
		- Padding oracle attacks
		- Hardcoded keys in client-side code
- ## Phase 4: Key & Secret Discovery
	- **Source Code / Config Exposure**
		- ```bash
		  gobuster dir -u http://target.com -w wordlist.txt -x .env,.config,.key
		  curl http://target.com/.env
		  curl http://target.com/.git/config
		  ```
	- **Look for:**
		- API keys in JavaScript files
		- Hardcoded credentials
		- Private keys in repositories
- ## Online Tools
	- ssllabs.com/ssltest - Comprehensive SSL test
	- crt.sh - Certificate transparency logs
	- hardenize.com - Security configuration check
- ## Defense
	- Use modern encryption (AES-256, RSA-2048+)
	- Enforce HTTPS everywhere
	- Proper key management (rotate, separate)
	- Salt and hash passwords (bcrypt, Argon2)
	- Use proven crypto libraries
