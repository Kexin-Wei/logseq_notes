# A01:2025 - Broken Access Control (BAC)

Attackers access resources or perform actions they shouldn't be authorized to do.

**Note**: SSRF is now included in this category in OWASP 2025
- ## How It Works
- a) **IDOR & Direct Access**
	- Three-phase attack:
		- 1. **Enumerate**: Discover all API endpoints and URLs (via directory brute-forcing, robots.txt, sitemaps)
		- 2. **Fetch**: Try accessing endpoints without authentication or with low-privilege credentials
		- 3. **Escalate**: Modify user IDs, access admin endpoints, or manipulate tokens to gain elevated privileges
- b) **Server-Side Request Forgery (SSRF)**
	- Trick server into making requests to unintended locations
	- Access internal services not exposed to internet
	- Steal cloud metadata (IAM credentials, API keys)
	- Port scan internal network
	- Bypass filters with obfuscated URLs
- ## Attack Vectors
- **Direct Object Reference:**
	- ```
	  GET /api/user/123/profile  → Change to /api/user/456/profile
	  GET /admin/dashboard       → Access without admin role
	  POST /api/user/promote     → Escalate own privileges
	  ```
- **SSRF:**
	- ```
	  http://localhost:3306                         -- MySQL database
	  http://169.254.169.254/latest/meta-data/      -- AWS metadata
	  http://metadata.google.internal/              -- GCP metadata
	  0x7f.0.0.1 / 127.1 / 2130706433              -- Obfuscated localhost
	  file:///etc/passwd                            -- File protocol
	  ```
- ## Real-World Examples
- **Instagram (2019)**: Users could view private photos by manipulating photo IDs in URLs
- **Parler (2021)**: Sequential post IDs allowed scraping all private posts
- **Capital One (2019)**: SSRF on AWS metadata endpoint exposed 100M+ records
- **Shopify (2020)**: SSRF to access internal Google Cloud services
- **Vend POS (2020)**: SSRF allowed reading AWS credentials
- **IDOR**: Changing `user_id=123` to `user_id=456` in URL reveals other users' data
- **Horizontal escalation**: Regular user accesses another user's account
- **Vertical escalation**: Regular user gains admin privileges
- ## Defense
- Implement proper authorization checks at every level
- Use least privilege principle
- Deny by default
- Log access control failures
- Whitelist allowed URLs/domains (SSRF)
- Disable unnecessary protocols: `file://`, `gopher://` (SSRF)
- Network segmentation
- Block access to cloud metadata endpoints