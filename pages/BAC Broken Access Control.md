- Attackers access resources or perform actions they shouldn't be authorized to do.
- **Note**: SSRF is now included in this category in OWASP 2025
- **Execution Order:** `Phase 1 → (2-8 parallel)` - Recon must complete first, then all other phases can run in parallel
- ## Phase 1: Reconnaissance & Enumeration
	- Discover all API endpoints, URLs, parameters
	- Map application structure (robots.txt, sitemaps, directory brute-forcing)
	- Identify user roles and privilege levels
	- Find parameters that accept URLs, file paths, or object references
- ## Phase 2: Missing Authentication & Function-Level Access Control
	- **Unauthenticated access**: Try accessing authenticated endpoints without login
	- **Low-privilege access**: Use regular user credentials to access admin/privileged endpoints
	- **HTTP method tampering**: If GET is protected, try POST/PUT/DELETE
	- **API endpoint access**: Test if API has same protections as web UI
- ## Phase 3: Horizontal Privilege Escalation (IDOR)
	- **Modify object references**: Change user IDs, document IDs, account numbers
		- ```
		  /api/user/123/records → /api/user/124/records
		  ```
	- **Test across all CRUD operations**: GET, POST, PUT, DELETE
	- **Try different formats**: Numeric IDs, UUIDs, encoded values
- ## Phase 4: Vertical Privilege Escalation
	- **Forced browsing**: Directly access admin URLs as regular user
		- ```
		  /app/getAppInfo → /app/admin_getAppInfo
		  ```
	- **Parameter tampering**:
		- Modify cookies, hidden fields
		- JWT manipulation: Change role claims `{"role":"user"}` → `{"role":"admin"}`
		- Replay tokens after logout
	- **Privilege escalation**: Act as admin while logged in as user
- ## Phase 5: SSRF (Server-Side Request Forgery)
	- **Find URL parameters**: `?url=`, `?image=`, `?callback=`, `?webhook=`, `?fetch=`
	- **Test internal access**:
		- ```
		  http://localhost:8080/admin
		  http://127.0.0.1
		  http://192.168.1.1, http://10.0.0.1
		  ```
	- **Cloud metadata endpoints**:
		- ```
		  AWS:   http://169.254.169.254/latest/meta-data/
		  Azure: http://169.254.169.254/metadata/instance
		  GCP:   http://metadata.google.internal/
		  ```
	- **File protocols**: `file:///etc/passwd`, `file:///c:/windows/system.ini`
	- **Obfuscation**: `0x7f.0.0.1`, `127.1`, `2130706433`
- ## Phase 6: Path Traversal
	- **Directory traversal**: `../../etc/passwd`, `..\..\windows\system32\config\sam`
	- **File access**: Test file download/upload endpoints
	- **URL encoding**: `%2e%2e%2f`, `%252e%252e%252f` (double encoding)
- ## Phase 7: CORS Misconfiguration
	- Test if sensitive endpoints allow requests from unauthorized origins
	- Check `Access-Control-Allow-Origin` headers
	- Try null origin, arbitrary origins
- ## Phase 8: Additional BAC Issues
	- **Mass assignment**: Add admin fields to user update requests
	- **Insecure defaults**: Check if resources are public by default
	- **Hidden functionality**: Test backup files, `.git` directories, hidden admin panels
- ## Real-World Examples
	- **Instagram (2019)**: Users could view private photos by manipulating photo IDs in URLs
	- **Parler (2021)**: Sequential post IDs allowed scraping all private posts
	- **Capital One (2019)**: SSRF on AWS metadata endpoint exposed 100M+ records
	- **Shopify (2020)**: SSRF to access internal Google Cloud services
	- **Vend POS (2020)**: SSRF allowed reading AWS credentials
- ## Defense
	- Implement proper authorization checks at every level
	- Use least privilege principle
	- Deny by default
	- Log access control failures
	- Whitelist allowed URLs/domains (SSRF)
	- Disable unnecessary protocols: `file://`, `gopher://` (SSRF)
	- Network segmentation
	- Block access to cloud metadata endpoints