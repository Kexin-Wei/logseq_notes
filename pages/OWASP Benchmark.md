- OWASP Benchmark for Java (v1.2) — 2,740 test cases for evaluating vulnerability detection tools.
- See also: [[LLM-Assisted Penetration Testing]], [[OWASP Top 10 (2025)]]
- ## Overview
	- The OWASP Benchmark for Java (v1.2) is a test suite with **2,740 test cases** for evaluating vulnerability detection tools (SAST, DAST, IAST).
	- **Location**: `/home/kexin/Repos/pentest/Achilles/configs/owasp-benchmark`
- ## Vulnerabilities Covered (11 Categories)
	- | Category | Count | CWE | Description |
	  |----------|-------|-----|-------------|
	  | SQL Injection (sqli) | 504 | CWE-89 | Database query injection |
	  | Weak Randomness (weakrand) | 493 | CWE-330 | Insecure random number generation |
	  | Cross-Site Scripting (xss) | 455 | CWE-79 | Reflected/stored XSS |
	  | Path Traversal (pathtraver) | 268 | CWE-22 | Directory traversal |
	  | Command Injection (cmdi) | 251 | CWE-78 | OS command execution |
	  | Cryptographic Issues (crypto) | 246 | CWE-327 | Weak cryptography (DES) |
	  | Weak Hash Functions (hash) | 236 | CWE-328 | MD5, SHA1 usage |
	  | Trust Boundary (trustbound) | 126 | CWE-501 | Trust boundary violations |
	  | Insecure Cookies (securecookie) | 67 | CWE-614 | Missing security attributes |
	  | LDAP Injection (ldapi) | 59 | CWE-90 | LDAP filter injection |
	  | XPath Injection (xpathi) | 35 | - | XPath expression injection |
	- **Total: 2,740 test cases**
- ## Ground Truth
	- **File**: `expectedresults-1.2.csv`
	- **Format**: CSV with 4 columns
	- ```csv
	  test name, category, real vulnerability, cwe
	  BenchmarkTest00001,pathtraver,true,22
	  BenchmarkTest00009,hash,false,328
	  BenchmarkTest00013,xss,true,79
	  ```
	- Fields: **test name** (`BenchmarkTest{5-digit ID}`), **category** (vuln type), **real vulnerability** (`true`/`false`), **cwe** (CWE number)
- ## Deployment
	- ```bash
	  cd /home/kexin/Repos/pentest/Achilles/configs/owasp-benchmark
	  docker-compose up -d
	  # Wait ~120 seconds for health check
	  # Available at: https://localhost:8443/benchmark/
	  ```
- ## Endpoint Pattern
	- ```
	  POST https://localhost:8443/benchmark/{vuln-type}-{variant}/{test-class}
	  ```
	- | Vulnerability | Endpoint | Input |
	  |---------------|----------|-------|
	  | Path Traversal | `/pathtraver-00/BenchmarkTest00001` | Cookie |
	  | Command Injection | `/cmdi-00/BenchmarkTest00006` | Header |
	  | SQL Injection | `/sqli-00/BenchmarkTest00008` | Header |
	  | XSS | `/xss-00/BenchmarkTest00013` | Header |
	  | LDAP Injection | `/ldapi-00/BenchmarkTest00012` | Header |
- ## Manual Validation Examples
	- ```bash
	  # Path Traversal
	  curl -k -X POST https://localhost:8443/benchmark/pathtraver-00/BenchmarkTest00001 \
	    -b "BenchmarkTest00001=../../../etc/passwd"
	  # Command Injection
	  curl -k -X POST https://localhost:8443/benchmark/cmdi-00/BenchmarkTest00006 \
	    -H "BenchmarkTest00006: ; whoami"
	  # SQL Injection
	  curl -k -X POST https://localhost:8443/benchmark/sqli-00/BenchmarkTest00008 \
	    -H "BenchmarkTest00008: ' OR 1=1 --"
	  ```
- ## Key Files
	- | Path | Purpose |
	  |------|---------|
	  | `expectedresults-1.2.csv` | Ground truth (2,740 tests) |
	  | `src/main/java/org/owasp/benchmark/testcode/` | Test case source code |
	  | `data/openapi.yaml` | API specification |
	  | `docker-compose.yml` | Container deployment |
	  | `pom.xml` | Maven build config |
- ## Validation Metrics
	- **TP**: Correctly identified vulnerability | **FP**: Safe code flagged as vulnerable | **TN**: Correctly identified safe code | **FN**: Missed vulnerability
	- `Accuracy = (TP + TN) / (TP + TN + FP + FN)`
- ## Notes
	- Each category has both vulnerable (`true`) and safe (`false`) variants
	- Input sources vary: cookies, headers, query parameters
	- OpenAPI spec (`data/openapi.yaml`) documents all endpoints
