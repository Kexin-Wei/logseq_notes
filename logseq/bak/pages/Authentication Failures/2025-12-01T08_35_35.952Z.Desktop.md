# A07:2025 - Authentication Failures

Weaknesses in authentication mechanisms allowing unauthorized access.

## How It Works

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

## Real-World Examples

- **Twitter (2022)**: 5.4M accounts exposed due to authentication API flaw
- **Mirai Botnet**: Exploited default credentials on IoT devices (`admin:admin`)
- **LinkedIn breach**: Weak password hashing led to mass credential theft
- **GitHub (2013)**: Session fixation vulnerability allowed account takeover

## Defense

- Strong password policies
- Multi-factor authentication
- Rate limiting on login attempts
- Secure session management
- Account lockout mechanisms
