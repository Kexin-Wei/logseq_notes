# A10:2025 - Mishandling of Exceptional Conditions

Failures to properly handle errors, edge cases, and unexpected inputs.

## How It Works

- a) Information Disclosure
	- Stack traces revealing system details
	- Error messages exposing database schema
- b) Resource Exhaustion
	- No limits on file uploads
	- Memory leaks on malformed input
- c) Improper Input Validation
	- Crashes on unexpected data types
	- Integer overflow/underflow
- d) Null Pointer Exceptions
	- Unhandled null values causing denial of service

## Real-World Examples

- **Cloudflare (2017)**: Cloudbleed leaked customer data due to buffer overflow
- **Apple iMessage (2019)**: Malformed message could crash devices
- **WhatsApp (2019)**: Specially crafted video file caused buffer overflow
- **Various**: Zip bombs causing resource exhaustion

## Defense

- Graceful error handling
- Input validation and bounds checking
- Resource limits and timeouts
- Fail securely (fail closed, not open)
- Comprehensive exception handling
- Generic error messages to users
