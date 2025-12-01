# A02:2025 - Security Misconfiguration

Insecure default configurations, incomplete setups, or exposed services.

## How It Works

- a) Default Credentials
	- Exploiting unchanged defaults: `admin:admin`, `root:root`
- b) Exposed Services
	- Databases, admin panels exposed to internet
	- Unnecessary open ports
- c) Security Headers
	- Missing: `X-Frame-Options`, `HSTS`, `CSP`
	- Misconfigured CORS policies
- d) Error Handling
	- Verbose error messages exposing stack traces
	- Database errors revealing schema
- e) Directory Listing
	- Exposed config files, backups, `.git` folders

## Real-World Examples

- **Equifax (2017)**: Unpatched Apache Struts led to 147M records stolen
- **MongoDB ransomware**: 27,000+ databases exposed due to no authentication
- **AWS S3 buckets**: Capital One breach (106M customers) due to misconfigured firewall
- **Elasticsearch clusters**: Healthcare data exposed due to default configs

## Defense

- Change all default credentials
- Disable directory listing
- Minimize exposed services
- Implement proper error handling
- Regular security configuration reviews

## How to Identify

### 1. Unnecessary Features Left On

- **Port Scanning**
	- ```bash
	  nmap -sV target-ip-address         # Basic scan
	  nmap -Pn -sS -sV -p- target-ip    # Detailed scan
	  ```
- **Directory/File Enumeration**
	- ```bash
	  gobuster dir -u http://target.com -w wordlist.txt
	  ```
- **Look for:**
	- Admin panels: /admin, /administrator, /phpmyadmin
	- API docs: /api/docs, /swagger, /graphql
	- Debug endpoints: /debug, /trace, /_debug
	- Version control: /.git, /.svn
	- Test/sample apps
	- Database management tools
- **Check HTTP headers:**
	- ```bash
	  curl -I http://target.com
	  ```

### 2. Overly Detailed Error Messages

- **Trigger Errors Intentionally**
	- ```bash
	  # SQL injection to trigger errors
	  http://target.com/page?id=1'

	  # Invalid parameters
	  http://target.com/api/user?id=abc

	  # File inclusion attempts
	  http://target.com/page?file=nonexistent.php
	  ```
- **Bad Error Messages Reveal:**
	- Database usernames and internal IPs
	- File paths and directory structure
	- Exact software versions
	- Stack traces with line numbers
- **Good Error Messages:**
	- Generic: "An error occurred. Please try again later."
	- Reference ID for support: "Error ID: #12345"
- **Testing Methods:**
	- Submit invalid form data
	- Try non-existent pages
	- Send malformed requests
	- Test auth with wrong credentials
	- Upload invalid file types

### 3. Missing Security Updates/Features

- **Version Detection**
	- ```bash
	  curl -I http://target.com
	  # Look for: Server, X-Powered-By, X-AspNet-Version headers
	  ```
- **Security Headers Check**
	- ✅ **Should Have:**
		- `Strict-Transport-Security: max-age=31536000`
		- `X-Content-Type-Options: nosniff`
		- `X-Frame-Options: DENY`
		- `Content-Security-Policy: default-src 'self'`
		- `X-XSS-Protection: 1; mode=block`
	- ❌ **Red Flags:**
		- Old server versions (Apache/2.2.x)
		- Missing security headers
		- Verbose version information
- **Vulnerability Scanners**
	- ```bash
	  nikto -h http://target.com        # Web server scan
	  sslscan target.com                # SSL/TLS check
	  testssl.sh target.com             # TLS configuration
	  ```
- **Check For:**
	- Outdated software with known CVEs
	- Weak SSL/TLS ciphers
	- Missing security headers
	- Debug mode enabled
	- Directory listing enabled

### Quick Check Workflow

- **Step 1: Reconnaissance**
	- ```bash
	  nmap -sV -sC target.com
	  nikto -h http://target.com
	  ```
- **Step 2: Enumeration**
	- ```bash
	  gobuster dir -u http://target.com -w common.txt
	  ```
- **Step 3: Error Testing**
	- Try invalid inputs on forms
	- Test authentication endpoints
	- Submit unexpected file types
- **Step 4: Configuration Review**
	- Check security headers
	- Verify SSL/TLS settings
	- Look for verbose errors
	- Test default credentials
- **Step 5: Version Analysis**
	- Compare versions against CVE databases
	- Check if security patches applied

### Quick Check Commands

- ```bash
  # Check headers
  curl -I https://target.com | grep -E "Server|X-Powered|X-AspNet"

  # Check common admin panels
  for path in admin administrator wp-admin phpmyadmin; do
    curl -s -o /dev/null -w "%{http_code} - /$path\n" http://target.com/$path
  done
  ```

### Online Tools

- securityheaders.com - Check HTTP headers
- ssllabs.com/ssltest - Test SSL configuration
- observatory.mozilla.org - Overall security scan
