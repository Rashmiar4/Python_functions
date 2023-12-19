#!/usr/bin/env python
# coding: utf-8

# # Abstraction example program

# In[1]:


from abc import ABC, abstractmethod

# Abstract class representing a Shape
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

# Concrete class Circle inheriting from Shape
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def display_info(self):
        print(f"Circle - Color: {self.color}, Radius: {self.radius}, Area: {self.area()}")

# Concrete class Rectangle inheriting from Shape
class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def display_info(self):
        print(f"Rectangle - Color: {self.color}, Length: {self.length}, Width: {self.width}, Area: {self.area()}")

# Usage of the classes
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)

circle.display_info()
rectangle.display_info()


# In[ ]:


#Explanation

# 1. `Shape` is an abstract base class with two abstract methods, `area` and `display_info`. This class cannot be instantiated directly but serves as a blueprint for other shapes.

# 2. `Circle` and `Rectangle` are concrete classes that inherit from the abstract class `Shape`. They provide implementations for the abstract methods `area` and `display_info`.

# 3. Both `Circle` and `Rectangle` have their own specific attributes (radius for Circle, length and width for Rectangle) and a common attribute `color` inherited from the `Shape` class.

# 4. The `display_info` method in each concrete class prints information about the shape, including its color and calculated area.

# 5. Finally, an instance of `Circle` and `Rectangle` is created, and their `display_info` methods are called to demonstrate abstraction and polymorphism in action.

