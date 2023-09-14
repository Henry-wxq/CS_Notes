"""
1) Class: Almost everything in Python is an object, with its properties and methods. A Class is like an object
   constructor, or a "blueprint" for creating objects. Classes provide a means of bundling data and
   functionality together.
2) Creating a new class creates a new type of object, allowing new instances of that type to be made.
2) All methods in a class require an object of that class as the first argument
"""
# ---------------------------------------- Create Class & Instances ----------------------------------------
from math import pi


class Circle(object):  # Create a class, the class name is Circle
    pass  # Can add properties and methods


circle1 = Circle()
circle2 = Circle()

# ---------------------------------------- Instances Properties ----------------------------------------
# Instances Properties: To distinguish different Instances; The individual property of each instance
circle1.r = 1  # r is the Instance Property
circle2.R = 2
print(circle1.r)  # Use InstanceName.PropertyName can get access to the property
print(circle2.R)

# __init__(): When creating instance, __init__() method will be automatically used to create an instance property
# for the created object. (Don't need to create different name when creating the instance property)


class Circle1(object):
    def __init__(self, r):  # Don't forget the parameter 'self'; it's the needed property of all method under class
        self.r = r


circle3 = Circle1(1)
circle4 = Circle1(2)
print(circle3.r)
print(circle4.r)
'''
Making sure that r in self.r is the instance property name; r in (self, r)is the parameter name
>>> class Circle1(object):
        def __init__(self, b):
            self.r = b
>>> circle5 = Circle(1)
>>> print(circle5.r) 
What we get access is the r not b
'''

# ---------------------------------------- Class Properties ----------------------------------------
# Class Properties: The shared property of all instances


class Circle2(object):
    pi1 = pi

    def __init__(self, r):
        self.r = r


circle6 = Circle2(3)
print('circle6.pi = ', circle6.pi1)

# Modify through ClassName will modify the class property
# Modify through InstanceName.ClassProperty actually create a new object property that have the
# same name as class property
Circle2.pi1 = 3.14
print('circle6.pi = ', circle6.pi1)
circle6.pi1 = 3.14159
print('circle6.pi = ', circle6.pi1)

# When accessing, instance property has higher precedence than the class property
# as shown above in circle6.pi1, when the names of instance property and class property are same
# need to delete the instance property to get access to the class property
del circle6.pi1
print('circle6.pi = ', circle6.pi1)

# ---------------------------------------- Method in Class ----------------------------------------


class Circle3(object):
    pi2 = pi

    # a special method
    def __init__(self, r):
        self.r = r

    # Use def to define a method, the first parameter should be 'self', which represents an object
    def get_area(self):
        """Surface of a circle"""
        # return self.r ** 2 * Circle.pi: modify through InstanceName.ClassProperty don't have impact
        return self.r ** 2 * self.pi2


circle7 = Circle3(4)
# When using a method in Class, no need to give a value to self, but don't forget the parentheses
print('Area of circle7 is ', circle7.get_area())
