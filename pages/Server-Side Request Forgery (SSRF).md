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