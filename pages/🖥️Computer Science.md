# The OWASP Top 10 Categories
	- | Category | Primary Defenses |
	  |----------|-----------------|
	  | **A01: BAC** | Authorization checks, least privilege, deny by default |
	  | **A02: Misconfiguration** | Change defaults, disable unnecessary features, security headers |
	  | **A03: Supply Chain** | Dependency audits, SBOM, version pinning, integrity checks |
	  | **A04: Cryptographic** | Strong algorithms, HTTPS, proper key management, salt passwords |
	  | **A05: Injection** | Parameterized queries, input validation, output encoding |
	  | **A06: Insecure Design** | Threat modeling, security requirements, rate limiting |
	  | **A07: Authentication** | MFA, strong passwords, rate limiting, secure sessions |
	  | **A08: Integrity** | Code signing, signature verification, secure CI/CD |
	  | **A09: Logging** | Comprehensive logging, real-time monitoring, tamper-proof storage |
	  | **A10: Exceptional Conditions** | Graceful error handling, input validation, resource limits |
	- **A01:2025** - [[BAC Broken Access Control]]
	- **A02:2025** - [[Security Misconfiguration]]
	- **A03:2025** - [[Software Supply Chain Failures]]
	- **A04:2025** - [[Cryptographic Failures]]
	- **A05:2025** - [[Injection]]
	- **A06:2025** - [[Insecure Design]]
	- **A07:2025** - [[Authentication Failures]]
	- **A08:2025** - [[Software or Data Integrity Failures]]
	- **A09:2025** - [[Logging & Alerting Failures]]
	- **A10:2025** - [[Mishandling of Exceptional Conditions]]
	- ## OWASP Pen Testing
		- | Category | Pen Test? | Notes |
		  |----------|-----------|-------|
		  | A01: BAC | ✅ Yes | IDOR, privilege escalation, access bypass |
		  | A02: Misconfiguration | ⚠️ Partial | Headers, defaults visible; internal configs not |
		  | A03: Supply Chain | ❌ No | Requires SBOM, dependency audit, pipeline access |
		  | A04: Cryptographic | ✅ Yes | TLS, certs, weak algorithms |
		  | A05: Injection | ✅ Yes | SQLi, XSS, command injection |
		  | A06: Insecure Design | ❌ No | Requires design/threat model review |
		  | A07: Authentication | ✅ Yes | Brute force, session, MFA bypass |
		  | A08: Integrity | ❌ No | Requires CI/CD, code signing audit |
		  | A09: Logging | ❌ No | Can't verify from outside |
		  | A10: Exceptional | ⚠️ Partial | Can trigger errors, can't verify handling |