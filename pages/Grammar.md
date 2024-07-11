- [cppiceberg](https://fouronnes.github.io/cppiceberg/)
- [abseil / C++ Quickstart With CMake](https://abseil.io/docs/cpp/quickstart-cmake.html)
- [Boost C++ Libraries](https://www.boost.org/)
- ## Constructor
  collapsed:: true
	- [The rule of three/five/zero - cppreference.com](https://en.cppreference.com/w/cpp/language/rule_of_three) #unread
- ## Destructor
  collapsed:: true
	- [Destructors, C++ FAQ (isocpp.org)](https://isocpp.org/wiki/faq/dtors)
	- [Destructors - cppreference.com](https://en.cppreference.com/w/cpp/language/destructor)
	- [When to Use Virtual Destructors in C++? - GeeksforGeeks](https://www.geeksforgeeks.org/when-to-use-virtual-destructors-in-cpp/)
- ## Enum
  collapsed:: true
	- [Enum Classes in C++ and Their Advantage over Enum DataType - GeeksforGeeks](https://www.geeksforgeeks.org/enum-classes-in-c-and-their-advantage-over-enum-datatype/)
	- [Enum vs Enum Class in C++ · Suneet Agrawal (agrawalsuneet.github.io)](https://agrawalsuneet.github.io/blogs/enum-vs-enum-class-in-c++/)
	- Enum just int inside
		- ```C++
		  #include <iostream>
		  
		  enum Day {
		      Sunday,     // 0
		      Monday,     // 1
		      Tuesday,    // 2
		      Wednesday,  // 3
		      Thursday,   // 4
		      Friday,     // 5
		      Saturday    // 6
		  };
		  
		  int main() {
		      Day today = Monday;
		      int dayValue = today; // Enum value directly used as an integer.
		      
		      std::cout << dayValue << std::endl; // Prints 1
		      return 0;
		  }
		  ```
	- Enum Class is safer
		- ```C++
		  #include <iostream>
		  
		  enum class Color {
		      Red,
		      Green,
		      Blue
		  };
		  
		  int main() {
		      Color myColor = Color::Red; // Enum value is scoped.
		      int Green = 42;             // No naming conflict.
		      
		      std::cout << static_cast<int>(myColor) << std::endl; // Prints 0 (Red)
		      return 0;
		  }
		  
		  #include <iostream>
		  
		  enum Color {
		      Red,
		      Green,
		      Blue
		  };
		  
		  int main() {
		      Color myColor = Red;
		      int myInt = 1;
		  
		      if (myColor == myInt) {
		          std::cout << "Colors match!" << std::endl; // Compiles, but unexpected behavior.
		      }
		  
		      return 0;
		  }
		  ```
		-
- ## Pointer
  collapsed:: true
	- [Pointer vs Reference Tutorial](https://www.geeksforgeeks.org/different-ways-to-use-const-with-reference-to-a-pointer-in-c/)
- ## td library
  collapsed:: true
	- [std::variant](https://en.cppreference.com/w/cpp/utility/variant)
	- [std::visit](https://en.cppreference.com/w/cpp/utility/variant/visit)
- ## Template
  collapsed:: true
	- In class / struct / function
		- ```C++
		  template <typename T>
		  struct Range
		  {
		      T min;
		      T max;
		      Range(T min = 0, T max = 0) :
		          min(min),
		          max(max)
		      {
		      }
		      bool operator==(const Range<T>& range) const
		      {
		          return (this->min == range.min && this->max == range.max);
		      }
		      template <typename T2>
		      bool operator==(const Range<T2>& range) const
		      {
		          return (this->min == range.min && this->max == range.max);
		      }
		  };
		  ```
		-
- ## Virtuality
  collapsed:: true
	- [Virtuality (gotw.ca)](http://www.gotw.ca/publications/mill18.htm)
- ## Polymorphism and Inheritance
  collapsed:: true
	- [Abstract Classes And Pure Virtual Functions](https://www.youtube.com/watch?v=wE0_F4LpGVc)
- ## Explicit
  id:: 668cd6b9-7368-48c8-b610-13c4fe6cd7ab
  collapsed:: true
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