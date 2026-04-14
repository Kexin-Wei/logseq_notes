- CWE (Common Weakness Enumeration) Top 25 Most Dangerous Software Weaknesses.
- See also: [[OWASP Top 10 (2025)]], [[Cybersecurity]]
- ## OWASP vs CWE: Different Purposes
	- | Aspect        | OWASP Top 10                          | CWE Top 25                                      |
	  | ------------- | ------------------------------------- | ------------------------------------------------ |
	  | Abstraction   | High-level risk categories            | Specific, concrete weakness types                |
	  | Audience      | Developers, organizations, compliance | Vulnerability researchers, CVE reporters, tools  |
	  | Scoring basis | Expert consensus + data               | Real-world CVE frequency + KEV exploitation data |
	  | Scope         | Web application security              | All software (including C/C++ system-level)      |
	  | Use case      | Security program planning, pentesting | Vulnerability classification, CVE tagging        |
- ## Memory Safety CWEs (no clean OWASP mapping)
	- Several CWE Top 25 entries are C/C++ memory safety bugs that fall outside OWASP's web-app focus:
		- CWE-787 Out-of-bounds Write (#5)
		- CWE-416 Use After Free (#7)
		- CWE-125 Out-of-bounds Read (#8)
		- CWE-120 Buffer Copy (#11)
		- CWE-190 Integer Overflow (#12)
		- CWE-119 Memory Corruption (#14)
- ## Which to Use
	- **OWASP Top 10** → high-level framework for organizing attack categories and compliance (PCI DSS, NIST)
	- **CWE IDs** → specific findings in reports, interoperable with NVD and vulnerability databases
	- For Achilles/Autopatch: use OWASP categories to organize test suites, tag each finding with CWE IDs for reporting.
