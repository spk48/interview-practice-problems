# Core Principles of Object Oriented Programming

## Encapsulation
Encapsulation is defined as the wrapping up of data under a single unit. It is the mechanism that binds together code and the data it manipulates. Other way to think about encapsulation is, it is a protective shield that prevents the data from being accessed by the code outside this shield.  

Encapsulation is the mechanism of hiding of data implementation by restricting access to public methods. Instance variables are kept private and accessor methods are made public to achieve this.

## Abstraction
Abstract means a concept or an Idea which is not associated with any particular instance. Using [abstract class](https://www.geeksforgeeks.org/abstract-classes-in-java/) or [Interface](https://www.geeksforgeeks.org/interfaces-in-java/) we express the intent of the class rather than the actual implementation. In a way, one class should not know the inner details of another in order to use it, just knowing the interfaces should be good enough.  

In short, abstraction is hiding the internal implementation of the feature and only showing the functionality to the users. i.e. what it works (showing), how it works (hiding). 

### Abstract Class vs. Interface 
1. **Type of methods**: Interface can have only abstract methods. Abstract class can have abstract and non-abstract methods. From Java 8, it can have default and static methods also.
2. **Final Variables**: Variables declared in a Java interface are by default final. An abstract class may contain non-final variables.
3. **Type of variables**: Abstract class can have final, non-final, static and non-static variables. Interface has only static and final variables.
4. **Implementation**: Abstract class can provide the implementation of interface. Interface can’t provide the implementation of abstract class.
5. **Inheritance vs Abstraction**: A Java interface can be implemented using keyword “implements” and abstract class can be extended using keyword “extends”.
6. **Multiple implementation**: An interface can extend another Java interface only, an abstract class can extend another Java class and implement multiple Java interfaces.
7. **Accessibility of Data Members**: Members of a Java interface are public by default. A Java abstract class can have class members like private, protected, etc.

## Inheritance
Inheritances expresses “is-a” and/or “has-a” relationship (composition) between two objects. Using Inheritance, In derived classes we can reuse the code of existing super classes. In Java, concept of “is-a” is based on class inheritance (using extends) or interface implementation (using implements).

## Polymorphism
It means one name many forms. It is further of two types — static and dynamic. Static polymorphism is achieved using method overloading and dynamic polymorphism using method overriding. It is closely related to inheritance. We can write a code that works on the superclass, and it will work with any subclass type as well.  

[Subtyping](https://en.wikipedia.org/wiki/Subtyping) - a form of polymorphism - is when calling code can be agnostic as to which class in the supported hierarchy it is operating on - the parent class or one of its descendants. Meanwhile, the same operation name among objects in an inheritance hierarchy may behave differently.