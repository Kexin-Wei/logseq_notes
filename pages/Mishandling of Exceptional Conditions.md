- Failures to properly handle errors, edge cases, and unexpected inputs.
- ## How It Works
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
- ## Real-World Examples
	- **Cloudflare (2017)**: Cloudbleed leaked customer data due to buffer overflow
	- **Apple iMessage (2019)**: Malformed message could crash devices
	- **WhatsApp (2019)**: Specially crafted video file caused buffer overflow
	- **Various**: Zip bombs causing resource exhaustion
- ## Phase 1: Error Message Analysis
	- **Trigger Errors Intentionally**
		- ```
		  # Invalid parameters
		  ?id=abc (when expecting int)
		  ?id=-1, ?id=99999999
		  ?id=null, ?id=undefined

		  # Malformed requests
		  Invalid JSON: {"key": }
		  Missing required fields
		  Wrong Content-Type
		  ```
	- **Look for in responses:**
		- Stack traces with line numbers
		- Database errors (table names, queries)
		- File paths and directory structure
		- Software versions
		- Internal IP addresses
- ## Phase 2: Input Boundary Testing
	- **Numeric Boundaries**
		- ```
		  0, -1, -999999999
		  2147483647 (INT_MAX)
		  2147483648 (INT_MAX + 1)
		  9999999999999999999
		  ```
	- **String Boundaries**
		- Empty string: `""`
		- Very long strings: 10000+ characters
		- Special characters: `\x00`, `\n`, `\r`
		- Unicode: emojis, RTL characters
	- **Array/Object Boundaries**
		- Empty arrays: `[]`
		- Deeply nested objects
		- Circular references
- ## Phase 3: Resource Exhaustion
	- **File Upload**
		- Very large files
		- Many simultaneous uploads
		- Zip bombs (small file, huge decompressed)
		- Polyglot files
	- **API Abuse**
		- ```bash
		  # Rapid requests
		  for i in {1..1000}; do curl http://target.com/api & done
		  ```
	- **Memory/CPU**
		- ReDoS: `(a+)+$` with `aaaaaaaaaaaaaaaa!`
		- XML bombs (billion laughs)
		- Large JSON payloads
- ## Phase 4: State Manipulation
	- **Race Conditions**
		- Simultaneous requests to same endpoint
		- Double-spend scenarios
	- **Null/Undefined Handling**
		- ```
		  null, undefined, NaN, Infinity
		  "", [], {}
		  ```
	- **Type Confusion**
		- String where int expected
		- Array where string expected
		- Object where array expected
- ## Phase 5: Fail-Open Testing
	- **Check if errors grant access**
		- Delete session cookie mid-request
		- Corrupt authentication token
		- Timeout during auth check
	- **Observe behavior on:**
		- Database connection failure
		- External service timeout
		- Rate limit exceeded
- ## Tools
	- Burp Intruder - Fuzzing
	- wfuzz - Web fuzzer
	- ffuf - Fast fuzzer
	- Radamsa - Mutation fuzzer
- ## Defense
	- Graceful error handling
	- Input validation and bounds checking
	- Resource limits and timeouts
	- Fail securely (fail closed, not open)
	- Comprehensive exception handling
	- Generic error messages to users
