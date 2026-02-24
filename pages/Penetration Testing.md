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
- Web application penetration testing methodology based on OWASP Top 10 2025.
- ## Testability Overview
	- | Category | Testable | Notes |
	  |----------|----------|-------|
	  | A01: BAC | ✅ Yes | IDOR, privilege escalation, SSRF |
	  | A02: Misconfiguration | ⚠️ Partial | External configs only |
	  | A03: Supply Chain | ❌ No | Requires internal access |
	  | A04: Cryptographic | ✅ Yes | TLS, certs, protocols |
	  | A05: Injection | ✅ Yes | SQLi, XSS, command injection |
	  | A06: Insecure Design | ❌ No | Requires design review |
	  | A07: Authentication | ✅ Yes | Brute force, sessions, MFA |
	  | A08: Integrity | ❌ No | Requires CI/CD access |
	  | A09: Logging | ❌ No | Can't verify externally |
	  | A10: Exceptional | ⚠️ Partial | Can trigger, can't verify handling |
- ## Execution Order Summary
	- | Category | Execution | Pattern |
	  |----------|-----------|---------|
	  | A01: BAC | Phase 1 → (2-8 parallel) | Recon first |
	  | A04: Crypto | All parallel | Independent tests |
	  | A05: Injection | Phase 1 → (2-5 parallel) | Discovery first |
	  | A07: Auth | Phase 1 → 2 → (3-6 parallel) | Recon → Creds → rest |
	  | A10: Exceptional | All parallel | Independent tests |
- ## Fully Testable Categories
- ### A01: Broken Access Control
	- See [[BAC Broken Access Control]]
	- **Execution:** `Phase 1 → (2-8 parallel)`
	- **Key Sections:**
		- Phase 1: Reconnaissance & Enumeration
		- Phase 2: Missing Authentication & Function-Level Access Control
		- Phase 3: Horizontal Privilege Escalation (IDOR)
		- Phase 4: Vertical Privilege Escalation
		- Phase 5: SSRF (Server-Side Request Forgery)
		- Phase 6: Path Traversal
		- Phase 7: CORS Misconfiguration
		- Phase 8: Additional BAC Issues
- ### A04: Cryptographic Failures
	- See [[Cryptographic Failures]]
	- **Execution:** `All parallel`
	- **Key Sections:**
		- Phase 1: TLS/SSL Analysis
		- Phase 2: Protocol Analysis
		- Phase 3: Cryptographic Implementation
		- Phase 4: Key & Secret Discovery
- ### A05: Injection
	- See [[Injection]]
	- **Execution:** `Phase 1 → (2-5 parallel)`
	- **Key Sections:**
		- Phase 1: Input Discovery
		- Phase 2: SQL Injection Testing
		- Phase 3: XSS Testing
		- Phase 4: Command Injection
		- Phase 5: Other Injection Types
- ### A07: Authentication Failures
	- See [[Authentication Failures]]
	- **Execution:** `Phase 1 → 2 → (3-6 parallel)`
	- **Key Sections:**
		- Phase 1: Reconnaissance
		- Phase 2: Password Testing
		- Phase 3: Session Management
		- Phase 4: MFA Bypass
		- Phase 5: Password Reset Flaws
		- Phase 6: OAuth/SSO Testing
- ## Partially Testable Categories
- ### A02: Security Misconfiguration
	- See [[Security Misconfiguration]]
	- **Key Sections:**
		- How to Identify (1-3)
		- Quick Check Workflow
	- **Limitations:** Internal configs, server settings not visible externally
- ### A10: Mishandling of Exceptional Conditions
	- See [[Mishandling of Exceptional Conditions]]
	- **Execution:** `All parallel`
	- **Key Sections:**
		- Phase 1: Error Message Analysis
		- Phase 2: Input Boundary Testing
		- Phase 3: Resource Exhaustion
		- Phase 4: State Manipulation
		- Phase 5: Fail-Open Testing
	- **Limitations:** Can observe external behavior, can't verify internal handling
- ## Not Testable via Pen Testing
- ### A03: Software Supply Chain Failures
	- See [[Software Supply Chain Failures]]
	- **Requires:** SBOM analysis, dependency audit, build pipeline access
- ### A06: Insecure Design
	- See [[Insecure Design]]
	- **Requires:** Threat modeling, architecture review, design documentation
- ### A08: Software or Data Integrity Failures
	- See [[Software or Data Integrity Failures]]
	- **Requires:** CI/CD pipeline access, code signing verification
- ### A09: Logging & Alerting Failures
	- See [[Logging & Alerting Failures]]
	- **Requires:** Log access, monitoring system review
- ## Essential Tools
	- **Reconnaissance:** nmap, gobuster, ffuf
	- **Proxy:** Burp Suite, OWASP ZAP
	- **Injection:** sqlmap, XSStrike, Commix
	- **Auth:** Hydra, CeWL, jwt_tool
	- **Crypto:** sslscan, testssl.sh
	- **Fuzzing:** wfuzz, Radamsa