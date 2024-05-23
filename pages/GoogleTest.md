- Concepts
	- ***Test***: assertion with result as *success*, *nonfatal failure*, or *fatal failure*
	- ***Test Suite***: a batch of tests
	- ***Test Program***: contain multiple test suites
- Assertions
	- are *macros*
	- use `EXPECT_*` when you want the test to continue to reveal more errors after the assertion failure, and use `ASSERT_*` when continuing after failure doesn’t make sense.
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
- CMake
	- Simple Project use `FetchContent`
		- ```CMake
		  # project CMakeLists.txt
		  cmake_minimum_required(VERSION 3.14)
		  project(my_project)
		  - *# GoogleTest requires at least C++14*
		  set(CMAKE_CXX_STANDARD 14)
		  set(CMAKE_CXX_STANDARD_REQUIRED ON)
		  - include(FetchContent)
		  FetchContent_Declare(
		  googletest
		  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
		  )
		  # For Windows: Prevent overriding the parent project's compiler/linker settings*
		  set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
		  FetchContent_MakeAvailable(googletest)
		  
		  
		  # myTest.cpp CMakeLists.txt
		  enable_testing()
		  
		  add_executable(myTest
		    myTest.cc
		  )
		  target_link_libraries(myTest
		    GTest::gtest_main
		  )
		  
		  include(GoogleTest)
		  gtest_discover_tests(hello_test)
		  ```
	- Use built version in big project and online server test
		- build googletest
			- Visual Studio need to set `gtest_force_shared_crt` ON
			- ```bash
			  git clone https://github.com/google/googletest.git -b v1.13.0
			  cd googletest        # Main directory of the cloned repository.
			  mkdir build          # Create a directory to hold the build output.
			  cd build
			  cmake ..             # Generate native build scripts for GoogleTest.
			  ```
		- add to project as a lib
			- ```cmake
			  # project CMakeLists.txt
			  # ...
			  set(CMAKE_CXX_STANDARD 14)
			  set(CMAKE_CXX_STANDARD_REQUIRED ON)
			  
			  set(GTest_DIR ${CMAKE_CURRENT_LIST_DIR}/googletest/lib/cmake/GTest)
			  
			  # For Windows: Prevent overriding the parent project's compiler/linker settings
			  set(gtest_force_shared_crt ON CACHE BOOL "" FORCE) 
			  
			  # if build as shared lib is on when building google test
			  set(GTEST_CREATE_SHARED_LIBRARY true) 
			  ```
		- same in test case CMakeLists.txt
			- ```cpp
			  # myTest.cpp CMakeLists.txt
			  enable_testing()
			  
			  add_executable(myTest
			    myTest.cc
			  )
			  target_link_libraries(myTest
			    GTest::gtest_main
			  )
			  
			  include(GoogleTest)
			  gtest_discover_tests(hello_test)
			  ```
- Google Test Example
	- ```cpp
	  #include <gtest/gtest.h>
	  
	  #include <QCoreApplication>
	  #include <QJsonArray>
	  #include <QJsonDocument>
	  #include <QJsonObject>
	  #include <QJsonValue>
	  #include <QResource>
	  
	  #include <infrastructure/utility/QJsonHelper.h>
	  using QJsonHelper = ultrast::infrastructure::utility::QJsonHelper;
	  
	  class QJsonHelperTest : public ::testing::Test
	  {
	  protected:
	      QJsonDocument testJson = QJsonDocument::fromJson(R"(
	          {
	              "string": "Hello, World!",
	              "number": 42,
	              "boolean": true,
	              "array": [1, 2, 3],
	              "object": {
	                  "key1": "value1",
	                  "key2": "value2"
	              },
	              "null": null
	          }
	          )");
	  };
	  
	  TEST_F(QJsonHelperTest, WriteAndReadPlainJson)
	  {
	      QFileInfo json("test.json");
	      ASSERT_TRUE(QJsonHelper::writePlainJson(json, testJson));
	  
	      QJsonDocument docRead = QJsonHelper::readPlainJson(json);
	      ASSERT_FALSE(docRead.isEmpty());
	      EXPECT_EQ(docRead["string"], "Hello, World!");
	      EXPECT_EQ(docRead["number"], 42);
	      EXPECT_EQ(docRead["boolean"], true);
	      EXPECT_EQ(docRead["array"], QJsonArray({ 1, 2, 3 }));
	      EXPECT_EQ(docRead["object"], QJsonObject({ { "key1", "value1" }, { "key2", "value2" } }));
	      EXPECT_EQ(docRead["null"], QJsonValue::Null);
	  }
	  
	  TEST_F(QJsonHelperTest, WriteAndReadEncryptedJson)
	  {
	      QFileInfo json("testEncrypted");
	      ASSERT_TRUE(ultrast::infrastructure::utility::QJsonHelper::writeEncryptedJson(json, testJson));
	  
	      QJsonDocument docRead = QJsonHelper::readEncryptedJson(json);
	      ASSERT_FALSE(docRead.isEmpty());
	      EXPECT_EQ(docRead["string"], "Hello, World!");
	      EXPECT_EQ(docRead["number"], 42);
	      EXPECT_EQ(docRead["boolean"], true);
	      EXPECT_EQ(docRead["array"], QJsonArray({ 1, 2, 3 }));
	      EXPECT_EQ(docRead["object"], QJsonObject({ { "key1", "value1" }, { "key2", "value2" } }));
	      EXPECT_EQ(docRead["null"], QJsonValue::Null);
	  }
	  
	  ```
- Reference
	- [GoogleTest User’s Guide](https://google.github.io/googletest/)
	- complete list of assertions: [Assertions Reference | GoogleTest](https://google.github.io/googletest/reference/assertions.html)
	- Matchers Reference: [Matchers Reference | GoogleTest](https://google.github.io/googletest/reference/matchers.html)