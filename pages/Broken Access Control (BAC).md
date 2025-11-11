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