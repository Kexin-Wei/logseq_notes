### [[Environment Set Up in Windows]]
- ### [[Code Review]]
- # Grammar
	- [cppiceberg](https://fouronnes.github.io/cppiceberg/)
	- [abseil / C++ Quickstart With CMake](https://abseil.io/docs/cpp/quickstart-cmake.html)
	- [Boost C++ Libraries](https://www.boost.org/)
	- Constructor
		- [The rule of three/five/zero - cppreference.com](https://en.cppreference.com/w/cpp/language/rule_of_three) #unread
	- Destructor
		- [Destructors, C++ FAQ (isocpp.org)](https://isocpp.org/wiki/faq/dtors)
		- [Destructors - cppreference.com](https://en.cppreference.com/w/cpp/language/destructor)
		- [When to Use Virtual Destructors in C++? - GeeksforGeeks](https://www.geeksforgeeks.org/when-to-use-virtual-destructors-in-cpp/)
	- Pointer
		- [Pointer vs Reference Tutorial](https://www.geeksforgeeks.org/different-ways-to-use-const-with-reference-to-a-pointer-in-c/)
	- std library
		- [std::variant](https://en.cppreference.com/w/cpp/utility/variant)
		- [std::visit](https://en.cppreference.com/w/cpp/utility/variant/visit)
	- template
	- virtuality
		- [Virtuality (gotw.ca)](http://www.gotw.ca/publications/mill18.htm)
	- polymorphism and inheritance
		- [Abstract Classes And Pure Virtual Functions](https://www.youtube.com/watch?v=wE0_F4LpGVc)
	- explicit
		- To prevent auto implicit conversion
			- implicit conversion
			  collapsed:: true
				- ```c++
				  int x = 5;
				  double y = x;  // Implicit conversion from int to double
				  
				  int a = 10;
				  double b = 3.14;
				  double result = a + b;  // Implicit conversion of 'a' to double before addition
				  ```
			- explicit conversion
			  collapsed:: true
				- ```c++
				  double x = 3.14;
				  int y = (int)x;  // C-style cast
				  
				  double x = 3.14;
				  int y = static_cast<int>(x);  // Static cast (recommended for most cases)
				  
				  Base* basePtr = new Derived();
				  Derived* derivedPtr = dynamic_cast<Derived*>(basePtr); // Dynamic cast (for polymorphic types):
				  
				  const int x = 5;
				  int* ptr = const_cast<int*>(&x); // Const cast (to add or remove const qualifier)
				  
				  int* ptr = new int(42);
				  long addr = reinterpret_cast<long>(ptr); // Reinterpret cast (for low-level reinterpretation of bit patterns)
				  ```
			- ```c++
			  class MyString {
			  public:
			      explicit MyString(int size) { /* ... */ }
			      MyString(const char* str) { /* ... */ }
			  };
			  
			  void printString(const MyString& s) { /* ... */ }
			  
			  int main() {
			      printString(10);  // Compile error: no implicit conversion allowed
			      printString("Hello");  // Still OK
			      printString(MyString(10));  // OK, explicit conversion
			  }
			  ```
		- Inheritance explicit
			- ```c++
			       B
			      / \
			     A   C
			      \ /
			       D
			       
			  class C : public B {
			  public:
			      explicit C(/* some parameters */) {
			          // Constructor implementation
			      }
			      // ...
			  };
			  
			  class D : public C {
			  public:
			      D(const A& a) : C(/* necessary arguments */) {
			          // Constructor implementation
			      }
			      // ...
			  };
			  ```
- # Threading
	-
- # C++ Unit Test
	- What is an unit test
		- Maintainable
		- Readable
		- Trustworthy
	- [[GoogleTest]]
	- [[Qt UnitTest]]
- # C++ code analysis
	- [Cppcheck - A tool for static C/C++ code analysis](https://cppcheck.sourceforge.io/)
	- [C/C++ Sanitizers | Microsoft Learn](https://learn.microsoft.com/en-us/cpp/sanitizers/?view=msvc-170)
	-
- Reference
	- [c++ faq - The Definitive C++ Book Guide and List - Stack Overflow](https://stackoverflow.com/questions/388242/the-definitive-c-book-guide-and-list)