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