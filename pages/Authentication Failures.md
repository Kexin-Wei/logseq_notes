- Weaknesses in authentication mechanisms allowing unauthorized access.
- **Execution Order:** `Phase 1 → 2 → (3-6 parallel)` - Recon first, then password testing (may need valid creds), then rest in parallel
- ## How It Works
	- a) Weak Passwords
		- No complexity requirements
		- Common passwords allowed
	- b) Brute Force
		- No rate limiting or account lockout
		- Missing CAPTCHA
	- c) Session Management
		- Session fixation attacks
		- Missing secure/httponly flags
		- No session timeout
	- d) MFA Bypass
		- Direct URL access skipping MFA
		- Session manipulation
	- e) Credential Recovery
		- Account enumeration via password reset
		- Weak reset tokens
- ## Real-World Examples
	- **Twitter (2022)**: 5.4M accounts exposed due to authentication API flaw
	- **Mirai Botnet**: Exploited default credentials on IoT devices (`admin:admin`)
	- **LinkedIn breach**: Weak password hashing led to mass credential theft
	- **GitHub (2013)**: Session fixation vulnerability allowed account takeover
- ## Phase 1: Reconnaissance
	- **Identify Authentication Endpoints**
		- `/login`, `/signin`, `/auth`, `/api/auth`
		- `/register`, `/signup`
		- `/forgot-password`, `/reset-password`
		- `/logout`, `/api/logout`
	- **Enumerate Users**
		- Different responses for valid vs invalid usernames
		- Timing differences in login responses
		- Password reset reveals valid emails
- ## Phase 2: Password Testing
	- **Default Credentials**
		- ```
		  admin:admin, admin:password, root:root
		  test:test, guest:guest
		  ```
	- **Brute Force**
		- ```bash
		  hydra -l admin -P wordlist.txt target.com http-post-form "/login:user=^USER^&pass=^PASS^:Invalid"
		  ```
	- **Password Spraying**
		- ```bash
		  # Try common passwords across many users
		  crackmapexec smb target -u users.txt -p 'Password123!'
		  ```
	- **Check for:**
		- Rate limiting / account lockout
		- CAPTCHA implementation
		- Password complexity requirements
- ## Phase 3: Session Management
	- **Session Token Analysis**
		- ```bash
		  # Check cookie attributes
		  curl -I http://target.com/login
		  # Look for: Secure, HttpOnly, SameSite flags
		  ```
	- **Session Fixation**
		- Does session ID change after login?
		- Can you set session ID before authentication?
	- **Session Hijacking**
		- Token predictability
		- Token transmitted over HTTP
	- **Session Timeout**
		- Does session expire?
		- Logout functionality works?
- ## Phase 4: MFA Bypass
	- **Direct Access**
		- After login, directly access protected pages
		- Modify response to skip MFA step
	- **Code Manipulation**
		- Brute force OTP codes
		- Reuse old codes
		- Try null/empty codes
	- **Backup Codes**
		- Test backup code limits
		- Check if codes are reusable
- ## Phase 5: Password Reset Flaws
	- **Token Analysis**
		- ```bash
		  # Check token predictability
		  # Request multiple tokens, compare patterns
		  ```
	- **Test for:**
		- Token expiration
		- Token reuse after password change
		- Host header injection
		- Token in URL (leaks via Referer)
- ## Phase 6: OAuth/SSO Testing
	- **OAuth Flaws**
		- Open redirect in redirect_uri
		- State parameter missing/weak
		- Token leakage
	- **SAML Attacks**
		- Signature bypass
		- XML injection
- ## Tools
	- Burp Suite - Session analysis
	- Hydra - Brute force
	- CeWL - Custom wordlist generator
	- jwt_tool - JWT analysis
- ## Defense
	- Strong password policies
	- Multi-factor authentication
	- Rate limiting on login attempts
	- Secure session management
	- Account lockout mechanisms
