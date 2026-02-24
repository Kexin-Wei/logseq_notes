# OWASP Top 10 (2025)
	- Reference for the OWASP Top 10 web application security risk categories.
	- See [[Penetration Testing]] for testability and methodology.
	- ## Categories & Primary Defenses
		- | Category | Primary Defenses |
		  |----------|-----------------|
		  | **A01:** [[BAC Broken Access Control]] | Authorization checks, least privilege, deny by default |
		  | **A02:** [[Security Misconfiguration]] | Change defaults, disable unnecessary features, security headers |
		  | **A03:** [[Software Supply Chain Failures]] | Dependency audits, SBOM, version pinning, integrity checks |
		  | **A04:** [[Cryptographic Failures]] | Strong algorithms, HTTPS, proper key management, salt passwords |
		  | **A05:** [[Injection]] | Parameterized queries, input validation, output encoding |
		  | **A06:** [[Insecure Design]] | Threat modeling, security requirements, rate limiting |
		  | **A07:** [[Authentication Failures]] | MFA, strong passwords, rate limiting, secure sessions |
		  | **A08:** [[Software or Data Integrity Failures]] | Code signing, signature verification, secure CI/CD |
		  | **A09:** [[Logging & Alerting Failures]] | Comprehensive logging, real-time monitoring, tamper-proof storage |
		  | **A10:** [[Mishandling of Exceptional Conditions]] | Graceful error handling, input validation, resource limits |