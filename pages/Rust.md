- Reference
	- https://rust-unofficial.github.io/too-many-lists/
- # Basic
	- use cargo to manage package
		- ```bash
		  cargo new PROJECT_NAME
		  cd PROJECT_NAME
		  cargo build
		  cargo run
		  cargo check # error debug
		  cargo fmt # format
		  ```
		- cargo project toml
			- ```toml
			  [workspace]
			  members = [
			      "Rust101/hello-rust",
			      "Rust101/print-a-string",
			      "Rust101/write-read-a-txt",
			      "Rust101/test-cargo",
			  ]
			  ```
-
- # Trouble shooting
	- [Ok & Error](https://www.sheshbabu.com/posts/rust-error-handling/)