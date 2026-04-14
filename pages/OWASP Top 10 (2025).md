- Reference for the OWASP Top 10 web application security risk categories.
  title:: OWASP Top 10 (2025)
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
- ## OWASP → CWE Mapping
	- See [[CWE Top 25]] for CWE overview and memory-safety CWEs.
	- | OWASP Category                               | CWE Top 25 Entries                                                       |
	  | --------------------------------------------- | ------------------------------------------------------------------------ |
	  | **A01 Broken Access Control**                 | CWE-862 (#4), CWE-863 (#17), CWE-284 (#19), CWE-639 (#24), CWE-22 (#6), CWE-352 (#3) |
	  | **A02 Security Misconfiguration**             | CWE-200 (#20), CWE-770 (#25)                                            |
	  | **A03 Software Supply Chain Failures**        | Not well represented (architectural/process concern)                     |
	  | **A04 Cryptographic Failures**                | Mostly below Top 25 (CWE-327, CWE-331)                                  |
	  | **A05 Injection**                             | CWE-79 (#1), CWE-89 (#2), CWE-78 (#9), CWE-94 (#10), CWE-77 (#23)     |
	  | **A06 Insecure Design**                       | No direct CWE Top 25 mapping (design-level concern)                      |
	  | **A07 Authentication Failures**               | CWE-306 (#21), CWE-798, CWE-287                                         |
	  | **A08 Software/Data Integrity Failures**      | CWE-502 (#15)                                                            |
	  | **A09 Logging & Alerting Failures**           | No direct CWE Top 25 mapping                                             |
	  | **A10 Mishandling of Exceptional Conditions** | CWE-476 (#13), CWE-20 (#18)                                             |