Introduction to OOP:

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects rather than functions and logic.

In traditional programming (procedural programming), we write functions and execute them step by step. But in OOP, we model real-world entities as objects that contain both data (attributes) and behavior (methods).

Python is an object-oriented programming language. In Python, almost everything is treated as an object.

The Four Pillars of OOP:

1️⃣ Encapsulation

Encapsulation means wrapping data and methods together inside a single unit (class) and restricting direct access to some data.

In simple words, it protects data from being accessed or modified directly from outside the class.

Encapsulation provides:

Data security

Controlled access

Better structure

In Python, encapsulation is achieved using:

Public members

Protected members (_variable)

Private members (__variable)

Encapsulation ensures that internal object data cannot be changed accidentally.

It is like a capsule where data is safely stored and accessed only through defined methods.

2️⃣ Abstraction

Abstraction means hiding internal implementation details and showing only the necessary functionality to the user.

The user interacts with simple interface without knowing complex internal logic.

Main purpose of abstraction:

Reduce complexity

Increase security

Improve readability

In real life:
When you use a mobile phone, you press buttons but you don’t know how internal circuits work.

In Python, abstraction can be implemented using:

Classes

Abstract classes (using abc module)

Abstraction focuses on what an object does, not how it does it.

3️⃣ Inheritance

Inheritance allows one class to inherit properties and methods from another class.

The class which gives features is called:

Parent class (Base class)

The class which receives features is called:

Child class (Derived class)

Benefits:

Code reusability

Reduced redundancy

Logical relationship representation

Inheritance types:

Single inheritance

Multiple inheritance

Multilevel inheritance

Hierarchical inheritance

Inheritance promotes DRY principle (Don’t Repeat Yourself).

4️⃣ Polymorphism

Polymorphism means “many forms”.

It allows same method name to behave differently for different objects.

There are two types:

Compile-time polymorphism (Method Overloading)

Runtime polymorphism (Method Overriding)

In Python:

True method overloading is not directly supported.

Method overriding is commonly used.

Polymorphism provides:

Flexibility

Extensibility

Cleaner code design

It allows writing generic code that works for multiple types.
