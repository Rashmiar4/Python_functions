#!/usr/bin/env python
# coding: utf-8

#  1)Difference between list and tuple in Python
# 
# 
# 1.	Mutability:
# •	List: Lists are mutable, which means you can modify their elements, add new elements, or remove existing elements after the list is created. You can use methods like append(), insert(), and remove() to modify a list.
# •	Tuple: Tuples are immutable, meaning once they are created, you cannot change, add, or remove elements. This immutability provides some advantages in terms of safety and performance for certain use cases.
# 2.	Syntax:
# •	List: Lists are created using square brackets []. For example: my_list = [1, 2, 3].
# •	Tuple: Tuples are created using parentheses (). For example: my_tuple = (1, 2, 3).
# 3.	Performance:
# •	List: Due to their mutability, lists may consume more memory than tuples. Modifying a list requires resizing and copying elements, which can be less efficient compared to tuples for certain operations.
# •	Tuple: Tuples, being immutable, can be more memory-efficient and might offer slightly better performance for certain operations.
# 4.	Use Cases:
# •	List: Use lists when you need a collection that can be modified, such as when you want to add, remove, or change elements during the program execution.
# •	Tuple: Use tuples when you want to create a collection that should remain constant throughout the program, or when you want to use the collection as a key in a dictionary (since keys in dictionaries must be immutable).
# 

# In[1]:


# List example
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Tuple example
my_tuple = (1, 2, 3)
# The following line would raise an error since tuples are immutable
# my_tuple.append(4)


# 2) concept of PEP 8.
# 
# PEP: Python Enhancement Proposal
# 8: The unique identifier for this particular proposal.
# 
# PEP 8 is a style guide for Python code that outlines conventions for writing clear, readable, and maintainable code. It covers various aspects of code formatting, including indentation, whitespace, naming conventions, and more. The primary purpose of PEP 8 is to encourage consistency across Python projects and enhance the overall quality of the codebase.
# 
# a.	Indentation: Use 4 spaces per indentation level. This is a widely accepted standard in the Python community.
# 
# b.	Maximum Line Length: Limit all lines to a maximum of 79 characters for code and 72 for docstrings. This promotes readability, especially when multiple files are open side by side.
# 
# c.	Imports: Imports should usually be on separate lines and should be grouped in the following order: standard library imports, related third-party imports, and then local application/library specific imports.
# 
# d.	Whitespace in Expressions and Statements: Avoid extraneous whitespace in the following situations: immediately inside parentheses, brackets, or braces; between a trailing comma and a following close parenthesis; and more.
# 
# e.	Naming Conventions:
# 
#     i.	Functions, variables, and attributes should be in lowercase with words separated by underscores (snake_case).
#     ii.	Classes should be in CamelCase.
#     iii.	Constants should be in uppercase with underscores separating words.
#     
# f.	Comments: Write comments sparingly and focus on explaining why something is done rather than what is done, as the latter should be clear from the code itself.
# 
# 

# 3) purpose of the __init__ method in Python classes
#  
#  
# In Python, the __init__ method plays a crucial role in classes as it serves as a constructor, automatically invoked when an object is instantiated from a class. Its primary purpose is to initialize the attributes of the object, providing a mechanism to set up the initial state of instances.
# 
# By defining the __init__ method within a class, developers can specify how the object should be initialized and what attributes it should possess. This method takes the instance itself (self) as its first parameter, followed by any additional parameters that the developer chooses to include.
# 
# Inside the __init__ method, instance variables are commonly created using self, allowing these attributes to be accessed throughout the class. The __init__ method facilitates parameterized initialization, enabling customization during object creation. This essential aspect of Python's object-oriented programming paradigm ensures that instances of a class start with a well-defined state, enhancing code organization, readability, and the overall maintainability of the software.
# 

# In[2]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Accessing instance variables
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30


# 4) How does inheritance work in Python? Provide an example.
# 
# Inheritance is a fundamental concept in object-oriented programming that allows a new class (subclass or derived class) to inherit attributes and behaviors from an existing class (superclass or base class). This promotes code reusability and the creation of a hierarchical structure. In Python, inheritance is implemented using the syntax class Subclass(BaseClass):, where Subclass is the new class inheriting from BaseClass.

# In[3]:


# Base class (superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


# Derived class (subclass)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


# Another derived class (subclass)
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Creating instances of the derived classes
dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")

# Using the speak method
print(dog_instance.speak())  # Output: Buddy says Woof!
print(cat_instance.speak())  # Output: Whiskers says Meow!


#  5) difference between staticmethod and classmethod.
#  
#  In Python, both staticmethod and classmethod are used to define methods that are bound to a class rather than an instance. However, they serve different purposes and have distinct behaviors:
#  
# 1.	staticmethod:
#     •	A method decorated with staticmethod is defined within a class but does not have access to the instance or the class itself as the first parameter.
# 
#     •	It is essentially a regular function that belongs to a class namespace, and it does not have access to self or cls automatically.
# 
#     •	It is often used for utility functions that are related to the class but do not depend on instance-specific or class-specific state.
# 
#     •	The staticmethod decorator is applied to a method using the @staticmethod syntax.
# 
# To call a static method, you don't need to create an instance of the class. You can call it using the class name.
# 

# classmethod:
# 
# •	A method decorated with classmethod is defined within a class and takes the class itself (cls) as its first parameter. This allows the method to access and modify class-level attributes.
# 
# •	It can also access the instance, but it is more commonly used to perform operations that involve the class itself rather than specific instances.
# 
# •	The classmethod decorator is applied to a method using the @classmethod syntax.
# 
# To call a class method, you use the class name.
# 

# In[6]:


class MyClass:
    class_variable = 10

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @staticmethod
    def static_method():
        return "This is a static method"

    @classmethod
    def class_method(cls):
        return f"This is a class method. Class variable: {cls.class_variable}"

# Using the static method
result_static = MyClass.static_method()
print(result_static)  # Output: This is a static method

# Using the class method
result_class = MyClass.class_method()
print(result_class)  # Output: This is a class method. Class variable: 10

# Creating an instance of MyClass
instance = MyClass(42)

# Calling the class method on an instance
result_instance = instance.class_method()
print(result_instance)  # Output: This is a class method. Class variable: 10


# 6) What is Polymorphism in Python? Give an example.
# 
# Polymorphism in Python refers to the ability of objects to take on multiple forms or, more specifically, the ability of different classes to be treated as instances of the same class through a common interface. This allows a single interface to represent various types of objects, providing flexibility and code reuse.
# 
# There are two types of polymorphism in Python: compile-time polymorphism (achieved through method overloading and operator overloading) and runtime polymorphism (achieved through method overriding).

# In[7]:


class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Duck(Animal):
    def speak(self):
        return "Quack!"


# Function that takes an Animal object and calls its speak method
def animal_sound(animal):
    return animal.speak()


# Creating instances of different subclasses
dog_instance = Dog()
cat_instance = Cat()
duck_instance = Duck()

# Calling the common interface method on different objects
print(animal_sound(dog_instance))  # Output: Woof!
print(animal_sound(cat_instance))  # Output: Meow!
print(animal_sound(duck_instance))  # Output: Quack!


# 7) How do you handle exceptions in Python?
# 
# In Python, exceptions are events that occur during the execution of a program that disrupts the normal flow of instructions. Exception handling allows you to gracefully manage these situations and respond to errors in a controlled manner. The try, except, else, and finally blocks are used for exception handling in Python.
# 
# 1.	Try Block:
# 
#     •	The code that may raise an exception is placed inside the try block.
# 
# 2.	Except Block:
# 
#     •	If an exception occurs within the try block, the corresponding except block is executed. This block contains the code that handles the exception.
# 
# 3.	Optional Else Block:
# 
#     •	The else block, if present, is executed only if no exceptions were raised in the try block.
# 
# 4.	Optional Finally Block:
# 
#     •	The finally block, if present, is executed regardless of whether an exception occurred. It is typically used for cleanup code that must be executed no matter what.
# 
# 

# In[8]:


def divide_numbers(a, b):
    try:
        result = a / b  # Division that may raise an exception
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid data type for division.")
    else:
        print("Division successful. Result:", result)
    finally:
        print("Executing the finally block.")

# Example usages
divide_numbers(10, 2)  # Output: Division successful. Result: 5.0 \n Executing the finally block.
divide_numbers(10, 0)  # Output: Error: Division by zero is not allowed. \n Executing the finally block.
divide_numbers("10", 2)  # Output: Error: Invalid data type for division. \n Executing the finally block.


# 8) Explain the Global Interpreter Lock (GIL) in Python.
# 
# The Global Interpreter Lock (GIL) is a mechanism inherent to the CPython interpreter, the default implementation of Python, designed to manage the execution of multiple threads.
# 
# This lock ensures that only one thread can execute Python bytecode at any given time within a single process. While the GIL simplifies memory management by making it thread-safe, it imposes limitations on the parallel execution of threads, impacting the performance of CPU-bound and multithreaded programs.
# 
# In scenarios where concurrency is critical, alternatives such as multiprocessing or asynchronous programming may be preferred. The GIL's influence is more pronounced in CPU-bound tasks, but for I/O-bound tasks, its impact is mitigated as threads can release the lock during waiting periods. 
# 
# It's essential to recognize that the GIL is specific to CPython, and alternative implementations of Python, such as Jython and IronPython, operate without a Global Interpreter Lock, allowing for more concurrent thread execution. As a trade-off between simplicity and performance, the GIL remains a notable characteristic of the CPython interpreter.

# 9) What is a decorator in Python? Provide an example.
# 
# In Python, a decorator is a design pattern that allows you to extend or modify the behavior of functions or methods without changing their actual code. 
# 
# Decorators are applied using the @decorator syntax above a function or method definition. They are a powerful feature used for aspects like logging, timing, access control, and more.

# In[9]:


# Decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

# Applying the decorator using the @ syntax
@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()


# 10) How do you implement encapsulation in Python
# 
# Encapsulation is one of the fundamental principles of object-oriented programming, and it refers to the concept of bundling data (attributes) and the methods that operate on the data into a single unit, known as a class. In Python, encapsulation is achieved through the use of private and protected attributes, as well as getter and setter methods.
# 
# Here's how encapsulation is implemented in Python:
# 
# Private Attributes:
# 
# Attributes that are intended to be private are prefixed with double underscores (__). This makes them name-mangled, and they are not directly accessible from outside the class.
# 
# Protected Attributes:
# 
# Attributes that are intended to be protected (accessible within the class and its subclasses) are prefixed with a single underscore (_). While this is more of a convention, it signals to other developers that the attribute is not intended to be used outside the class.
# 
# Getter and Setter Methods:
# 
# To access or modify private or protected attributes, getter and setter methods are used. Getter methods allow you to retrieve the value of an attribute, while setter methods allow you to modify it. These methods provide a controlled interface to the class's internal state.
# 
# 

# In[10]:


class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self._age = age     # Protected attribute

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, new_name):
        self.__name = new_name

    # Getter method for age
    def get_age(self):
        return self._age

    # Setter method for age
    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            print("Age cannot be negative.")

# Creating an instance of the Person class
person = Person("Alice", 30)

# Accessing attributes using getter methods
print("Name:", person.get_name())  
print("Age:", person.get_age())   

# Modifying attributes using setter methods
person.set_name("Bob")
person.set_age(25)

# Accessing modified attributes
print("Updated Name:", person.get_name())  
print("Updated Age:", person.get_age())    


# 11) Explain the concept of duck typing.
# 
# 
# Duck typing is a programming concept used in dynamically typed languages, including Python. The term "duck typing" comes from the saying, "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck." In the context of programming, duck typing implies that the type or class of an object is determined by its behavior (methods and properties) rather than its explicit type.
# 
# The key idea behind duck typing is that the suitability of an object for a particular operation is determined by whether the object can perform the required method or behavior, rather than by its inheritance or class hierarchy. This allows for more flexibility and less emphasis on formal type declarations.

# In[11]:


class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

class Duck:
    def sound(self):
        return "Quack!"

# Function using duck typing
def make_sound(animal):
    return animal.sound()

# Instances of different classes
dog_instance = Dog()
cat_instance = Cat()
duck_instance = Duck()

# Calling the function with different instances
print(make_sound(dog_instance))  
print(make_sound(cat_instance))  
print(make_sound(duck_instance)) 


# 12) difference between append() and extend() methods for lists
# 
# In Python, append() and extend() are two methods used to add elements to a list, but they behave differently:
# 
# 1.	append() Method:
# 
# •	The append() method is used to add a single element to the end of a list.
# 
# •	The element can be of any data type, including other lists.
# 
# •	The syntax is list.append(element), where element is the item to be added.
# 
# 

# In[12]:


my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  


# extend() Method:
# 
# The extend() method is used to add multiple elements from an iterable (e.g., a list, tuple, or string) to the end of a list.
# 
# It modifies the original list by adding each element from the iterable individually.
# 
# The syntax is list.extend(iterable), where iterable is the sequence of elements to be added.

# In[13]:


my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  


# 13) How does the with statement work in Python?
# 
# The with statement in Python serves as a powerful tool for simplifying resource management, particularly in scenarios involving file handling, network connections, or other situations where proper setup and cleanup are crucial. The key to the with statement lies in its ability to work with objects that implement the context management protocol by defining __enter__() and __exit__() methods.
# 
# Upon encountering a with statement, the expression following it is evaluated, and the result is assigned to a variable. The __enter__() method of the associated context manager is then invoked, facilitating the setup of necessary resources. Subsequently, the indented code block within the with statement is executed, during which the assigned variable can be utilized. Importantly, the __exit__() method is guaranteed to be called afterward, regardless of whether an exception occurs within the code block. This ensures proper cleanup, resource release, and exception handling.
# 
# A common use case is seen with file handling, where the open() function returns a file object compatible with the with statement. Upon exiting the with block, the file is automatically closed, streamlining the process of managing resources. The with statement exemplifies Python's commitment to readability and clean code, offering a concise and efficient approach to resource management in various programming contexts.

# 14) Discuss the use of self in Python classes.
# 
# In Python, the self keyword plays a fundamental role within class definitions, serving as a reference to the instance of the class itself. This convention is particularly crucial in instance methods, where self is used as the first parameter to enable access to and manipulation of instance attributes. It allows for the creation of object-specific data and fosters the encapsulation of behavior within classes. When an instance method is called, Python automatically passes the instance (self) as the first parameter, facilitating the interaction between the method and the specific instance. While using self is a convention and not mandatory, it significantly enhances code readability and adheres to established Python practices, making the code more understandable for other developers.

# In[14]:


class MyClass:
    def __init__(self, x):
        self.x = x

    def print_value(self):
        print(self.x)

    def update_value(self, new_x):
        self.x = new_x

# Creating an instance of MyClass
obj = MyClass(42)

# Accessing and printing the value using an instance method
obj.print_value()  # Output: 42

# Updating the value using another instance method
obj.update_value(99)

# Accessing and printing the updated value
print(obj.x)  # Output: 99


# 15) Explain the purpose of the __slots__ attribute.
# 
# 
# The __slots__ attribute in Python serves the purpose of defining a fixed set of attributes for instances of a class, restricting the creation of additional attributes. By specifying __slots__, developers can optimize memory usage and improve attribute access speed since the interpreter no longer needs to store a dynamic dictionary for each instance. This feature is particularly beneficial when dealing with a large number of instances where memory efficiency is critical.

# In[15]:


class MyClassWithSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Instances of MyClassWithSlots can only have 'x' and 'y' attributes
obj1 = MyClassWithSlots(10, 20)
obj2 = MyClassWithSlots(30, 40)

# Accessing attributes
print(obj1.x, obj1.y)  
print(obj2.x, obj2.y)  


# 16) What is the difference between an instance variable and a class variable?
# 
# Instance Variables:
# 
# Instance variables are associated with instances of a class.
# 
# Each instance of the class has its own copy of instance variables, and their values can vary between different instances.
# 
# They are defined inside the constructor method (__init__) using the self keyword.

# In[16]:


class MyClass:
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

obj1 = MyClass(10)
obj2 = MyClass(20)

print(obj1.instance_variable)  # Output: 10
print(obj2.instance_variable)  # Output: 20


# Class Variables:
# 
# Class variables are shared among all instances of a class.
# 
# They are defined outside any method, usually at the top of the class definition.
# 
# Class variables are accessed using the class name, not through instances.
# 

# In[17]:


class MyClass:
    class_variable = 0

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable
        MyClass.class_variable += 1

obj1 = MyClass(10)
obj2 = MyClass(20)

print(obj1.class_variable)  
print(obj2.class_variable)  


# How do you implement Encapsulation, Abstraction, Polymorphism?
# 
# 
# In Python, encapsulation is implemented by using private and protected attributes within class definitions, denoted by double and single underscores, respectively. Encapsulation ensures that the internal state of an object is hidden from external access, and methods provide controlled access to these attributes. Abstraction is achieved by defining abstract classes or interfaces using the abc module, allowing the creation of abstract methods that must be implemented by concrete subclasses. This enforces a common interface while hiding implementation details. Polymorphism is inherent in Python through dynamic typing and duck typing. Objects can take on multiple forms, and functions can operate on objects based on their behavior rather than their specific type, promoting flexibility and code reuse. The combination of encapsulation, abstraction, and polymorphism enables the development of modular, maintainable, and extensible code in Python's object-oriented paradigm.

# In[18]:


from abc import ABC, abstractmethod

# Encapsulation: Using private and protected attributes
class EncapsulationExample:
    def __init__(self):
        self._protected_attribute = "I am protected!"
        self.__private_attribute = "I am private!"

    def get_protected_attribute(self):
        return self._protected_attribute

    def set_protected_attribute(self, value):
        self._protected_attribute = value

    def get_private_attribute(self):
        return self.__private_attribute

    def set_private_attribute(self, value):
        self.__private_attribute = value

# Abstraction: Using abstract classes and methods
class AbstractAnimal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(AbstractAnimal):
    def make_sound(self):
        return "Woof!"

class Cat(AbstractAnimal):
    def make_sound(self):
        return "Meow!"

# Polymorphism: Objects taking on multiple forms
def animal_sounds(animal):
    return animal.make_sound()

# Creating instances
encapsulation_obj = EncapsulationExample()
dog = Dog()
cat = Cat()

# Encapsulation
print(encapsulation_obj.get_protected_attribute())  # Output: I am protected!
print(encapsulation_obj.get_private_attribute())    # Output: I am private!

# Abstraction and Polymorphism
print(animal_sounds(dog))  # Output: Woof!
print(animal_sounds(cat))  # Output: Meow!


# How do you Implement single level Inheritance, multiple level inheritance, multi level inheritance, Hybrid Inheritance
# 
# 
# Single Level Inheritance:
# 
# Single-level inheritance involves one base class and one derived class. The derived class inherits attributes and methods from a single base class. It establishes a straightforward parent-child relationship.

# In[19]:


class Parent:
    def display(self):
        print("This is the parent class.")

class Child(Parent):
    def show(self):
        print("This is the child class.")

# Single Level Inheritance
child_obj = Child()
child_obj.display()  # Output: This is the parent class.
child_obj.show()     # Output: This is the child class.


# Multiple Level Inheritance:
# 
# Multiple-level inheritance involves a chain of classes, where each class inherits from the one above it. The bottom-most class inherits attributes and methods from both the immediate parent and the ancestors.

# In[20]:


class Grandparent:
    def grand_display(self):
        print("This is the grandparent class.")

class Parent(Grandparent):
    def parent_display(self):
        print("This is the parent class.")

class Child(Parent):
    def child_display(self):
        print("This is the child class.")

# Multiple Level Inheritance
child_obj = Child()
child_obj.grand_display()  # Output: This is the grandparent class.
child_obj.parent_display() # Output: This is the parent class.
child_obj.child_display()  # Output: This is the child class.


# Multilevel Inheritance:
# 
# Multilevel inheritance involves a chain of classes, where each class inherits from the one immediately above it. It establishes a hierarchical relationship, and the derived class becomes the base class for subsequent classes.

# In[21]:


class Base:
    def base_display(self):
        print("This is the base class.")

class Intermediate(Base):
    def intermediate_display(self):
        print("This is the intermediate class.")

class Derived(Intermediate):
    def derived_display(self):
        print("This is the derived class.")

# Multilevel Inheritance
derived_obj = Derived()
derived_obj.base_display()         # Output: This is the base class.
derived_obj.intermediate_display() # Output: This is the intermediate class.
derived_obj.derived_display()       # Output: This is the derived class.


# Hybrid Inheritance:
# 
# Hybrid inheritance involves a combination of any two or more types of inheritance mentioned above within a single program. It can include single, multiple, multilevel, or any other combination of inheritance types.

# In[22]:


class A:
    def method_A(self):
        print("Method from class A.")

class B(A):
    def method_B(self):
        print("Method from class B.")

class C(A):
    def method_C(self):
        print("Method from class C.")

class D(B, C):
    def method_D(self):
        print("Method from class D.")

# Hybrid Inheritance
obj = D()
obj.method_A()  # Output: Method from class A.
obj.method_B()  # Output: Method from class B.
obj.method_C()  # Output: Method from class C.
obj.method_D()  # Output: Method from class D.


# In[ ]:




