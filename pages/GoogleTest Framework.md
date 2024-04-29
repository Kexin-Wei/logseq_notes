- Concepts
	- ***Test***: assertion with result as *success*, *nonfatal failure*, or *fatal failure*
	- ***Test Suite***: a batch of tests
	- ***Test Program***: contain multiple test suites
- Assertions
	- are *macros*
	- complete list of assertions: [Assertions Reference | GoogleTest](https://google.github.io/googletest/reference/assertions.html)
	- Matchers Reference: [Matchers Reference | GoogleTest](https://google.github.io/googletest/reference/matchers.html)
	- Example
	  ```C++
	  #include <gmock/gmock.h>
	  
	  using ::testing::AllOf;
	  using ::testing::Gt;
	  using ::testing::Lt;
	  using ::testing::MatchesRegex;
	  using ::testing::StartsWith;
	  
	  ...
	  EXPECT_THAT(value1, StartsWith("Hello"));
	  EXPECT_THAT(value2, MatchesRegex("Line \\d+"));
	  ASSERT_THAT(value3, AllOf(Gt(5), Lt(10)));
	  ```
- Test Example
	-
- Reference
	- [GoogleTest User’s Guide](https://google.github.io/googletest/)