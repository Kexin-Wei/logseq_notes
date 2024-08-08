## [[Environment Set Up in Windows]]
- ## [[Code Review]]
- # [[C++ Grammar]]
  :LOGBOOK:
  CLOCK: [2024-07-15 Mon 14:06:52]--[2024-07-15 Mon 14:06:52] =>  00:00:00
  :END:
- C++ Guidelines
	- [C++ Core Guidelines (isocpp.github.io)](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) #PICKME
		- [In: Introduction](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-introduction) ✔️
		- [P: Philosophy](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-philosophy)
		- [I: Interfaces](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-interfaces)
		- [F: Functions](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-functions)
		- [C: Classes and class hierarchies](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-class)
		- [Enum: Enumerations](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-enum)
		- [R: Resource management](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-resource)
		- [ES: Expressions and statements](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-expr)
		- [Per: Performance](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-performance)
		- [CP: Concurrency and parallelism](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-concurrency)
		- [E: Error handling](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-errors)
		- [Con: Constants and immutability](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-const)
		- [T: Templates and generic programming](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-templates)
		- [CPL: C-style programming](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-cpl)
		- [SF: Source files](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-source)
		- [SL: The Standard Library](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#sl-the-standard-library)
- ## Class UML
	- Association vs Composition vs Aggregation
		- ![image.png](../assets/image_1721626097937_0.png)
		- **Association** - I have a relationship with an object. `Foo` uses `Bar`
			- ```
			  public class Foo {         
			    private Bar bar;
			  };
			  ```
			  NB: See [Fowler's definition](https://martinfowler.com/bliki/DependencyAndAssociation.html) - the key is that `Bar` is semantically related to `Foo` rather than just a dependency (like an `int` or `string`).
		- **Composition** - I own an object and I am responsible for its lifetime. When `Foo` dies, so does `Bar`
			- ```
			  public class Foo {
			    private Bar bar = new Bar(); 
			  }
			  ```
		- **Aggregation** - I have an object which I've borrowed from someone else. When `Foo` dies, `Bar` may live on.
			- ```
			  public class Foo { 
			    private Bar bar; 
			    Foo(Bar bar) { 
			       this.bar = bar; 
			    }
			  }
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
- Reference
	- [c++ faq - The Definitive C++ Book Guide and List - Stack Overflow](https://stackoverflow.com/questions/388242/the-definitive-c-book-guide-and-list)