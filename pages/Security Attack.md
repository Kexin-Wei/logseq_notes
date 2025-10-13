## Broken Access Control (BAC)
	- Attackers access resources or perform actions they shouldn't be authorized to do.
	- ### How It Works
		- Three-phase attack:
			- 1. **Enumerate**: Discover all API endpoints and URLs (via directory brute-forcing, robots.txt, sitemaps)
			- 2. **Fetch**: Try accessing endpoints without authentication or with low-privilege credentials
			- 3. **Escalate**: Modify user IDs, access admin endpoints, or manipulate tokens to gain elevated privileges
	- ### Real-World Examples
		- **Instagram (2019)**: Users could view private photos by manipulating photo IDs in URLs
		- **Parler (2021)**: Sequential post IDs allowed scraping all private posts
		- **IDOR (Insecure Direct Object Reference)**: Changing `user_id=123` to `user_id=456` in URL reveals other users' data
		- **Horizontal escalation**: Regular user accesses another user's account
		- **Vertical escalation**: Regular user gains admin privileges
	- ### Attack Vectors
		- ```
		  GET /api/user/123/profile  → Change to /api/user/456/profile
		  GET /admin/dashboard       → Access without admin role
		  POST /api/user/promote     → Escalate own privileges
		  ```
- ## Authentication Failures
	- Weaknesses in authentication mechanisms allowing unauthorized access.
	- ### How It Works
		- a) Weak Passwords
			- Test common passwords: `password`, `123456`, `admin`
			- Check if password complexity is enforced
		- b) Brute Force
			- Make repeated login attempts
			- Test if rate limiting or account lockout exists
			- Check for CAPTCHA or anti-automation measures
		- c) Session Management
			- Session fixation attacks
			- Check secure/httponly cookie flags
			- Test if sessions invalidate on logout
			- Session hijacking attempts
		- d) MFA Bypass
			- Check if MFA can be bypassed via direct URL access
			- Test API endpoints that skip MFA
			- Session manipulation to avoid 2FA
		- e) Credential Recovery
			- Account enumeration via password reset
			- Weak/predictable reset tokens
			- Insecure security questions
	- ### Real-World Examples
		- **Twitter (2022)**: 5.4M accounts exposed due to authentication API flaw
		- **Mirai Botnet**: Exploited default credentials on IoT devices (`admin:admin`)
		- **LinkedIn breach**: Weak password hashing led to mass credential theft
		- **GitHub (2013)**: Session fixation vulnerability allowed account takeover
- ## Security Misconfiguration
	- Insecure default configurations, incomplete setups, or exposed services.
	- ### How It Works
		- a) Default Credentials
			- Test common defaults: `admin:admin`, `root:root`, `administrator:password`
			- Check SSH, databases, web panels
		- b) Exposed Services
			- Scan for open ports
			- Identify sensitive services exposed to internet (databases, admin panels)
			- Check management interfaces
		- c) Security Headers
			- Missing headers: `X-Frame-Options`, `X-Content-Type-Options`, `HSTS`, `CSP`
			- Misconfigured CORS policies
		- d) Error Handling
			- Verbose error messages exposing stack traces
			- Database errors revealing schema
			- Sensitive paths leaked
		- e) Directory Listing
			- Web server shows directory contents
			- Exposed config files, backups, `.git` folders
	- ### Real-World Examples
		- **Equifax (2017)**: Unpatched Apache Struts led to 147M records stolen
		- **MongoDB ransomware**: 27,000+ databases exposed due to no authentication
		- **AWS S3 buckets**: Capital One breach (106M customers) due to misconfigured firewall
		- **Elasticsearch clusters**: Healthcare data exposed due to default configs
- ## Injection Attacks
	- Untrusted data sent to interpreters as part of commands or queries.
	- ### How It Works
	- a) SQL Injection
		- Injecting SQL commands into database queries
		- ```sql
		  
		  ' OR '1'='1        -- Authentication bypass
		  
		  '; DROP TABLE users--  -- Destructive
		  
		  ' UNION SELECT password FROM users--  -- Data extraction
		  
		  ```
	- b) Command Injection
		- Executing system commands on the server
		- ```bash
		  ; whoami          -- Check current user
		  | ls -la           -- List files
		  && cat /etc/passwd -- Read sensitive files
		  `id`              -- Execute commands
		  ```
	- c) XSS (Cross-Site Scripting)
		- Injecting malicious JavaScript
		- ```html
		  <script>alert(document.cookie)</script>
		  <img src=x onerror=alert(1)>
		  <iframe src="javascript:alert(1)">
		  ```
	- ### Real-World Examples
		- **Sony Pictures (2011)**: SQL injection led to 1M accounts stolen
		- **British Airways (2018)**: XSS-based Magecart attack stole 380,000 payment cards
		- **Heartland Payment Systems**: SQL injection compromised 130M credit cards
		- **Yahoo (2012)**: SQL injection via union-based attack
- ## Server-Side Request Forgery (SSRF)
	- Attacker tricks server into making requests to unintended locations (internal network, cloud metadata).
	- ### How It Works
		- a) Internal Network Access
			- Access internal services not exposed to internet
			- ```
			  http://localhost:3306      -- MySQL database
			  http://192.168.1.10:22    -- Internal SSH
			  http://10.0.0.5:9200      -- Elasticsearch
			  ```
		- b) Cloud Metadata Endpoints
			- Steal IAM credentials, API keys
			- ```
			  http://169.254.169.254/latest/meta-data/  -- AWS
			  http://metadata.google.internal/          -- GCP
			  http://169.254.169.254/metadata/instance  -- Azure
			  ```
		- c) Port Scanning
			- Use server to scan internal network
			- ```
			  Test ports: 22, 80, 443, 3306, 5432, 6379, 9200, 27017
			  ```
		- d) Filter Bypass
			- Obfuscate payloads to bypass filters
			- ```
			  0x7f.0.0.1          -- Hex notation
			  127.1               -- Short form
			  2130706433          -- Decimal IP
			  file:///etc/passwd  -- File protocol
			  ```
		- ### Real-World Examples
			- **Capital One (2019)**: SSRF on AWS metadata endpoint exposed 100M+ records
			- **Shopify (2020)**: SSRF to access internal Google Cloud services
			- **Vend POS (2020)**: SSRF allowed reading AWS credentials
			- **Orange Tsai's PDF generator**: SSRF chain to RCE on multiple companies
- ## Common Attack Flow Example
	- 1. Reconnaissance → Find target IP: 192.168.0.103
	  
	  2. Network Scan → Discover open ports: 22 (SSH), 80 (HTTP), 8042 (HTTP)
	  
	  3. Misconfiguration → Test default creds: admin:admin works!
	  
	  4. Access Control → Enumerate endpoints: /api/users, /admin/panel
	  
	  5. BAC → Access /admin/panel without proper auth
	  
	  6. Injection → Test SQL injection on /api/users?id=1
	  
	  7. SSRF → Use file upload to access http://169.254.169.254/
	  
	  8. Privilege Escalation → Gain admin access via token manipulation
- ## Defense Recommendations
	- | Attack Type | Defense |
	  | **BAC** | Implement proper authorization checks, use least privilege principle |
	  | **Authentication** | Strong password policies, MFA, rate limiting, secure session management |
	  | **Misconfiguration** | Change defaults, disable directory listing, minimize exposed services |
	  | **Injection** | Input validation, parameterized queries, output encoding, CSP headers |
	  | **SSRF** | Whitelist allowed URLs, disable unnecessary protocols, network segmentation |
	  
	  These attacks represent the **OWASP Top 10** vulnerabilities and are the most common security flaws found in modern applications.