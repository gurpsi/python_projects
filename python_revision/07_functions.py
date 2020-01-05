import math


def f():
    pass


def ping():
    return 'Ping'


def volume(r):
    """Returns the volume of a sphere with radius r."""
    return (4/3) * math.pi * r**3


print(volume(2))


def triangle_area(b,h):
    """Returns the area of the triangle"""
    return 0.5 * b * h


print(triangle_area(5,5))


def cm(feet = 0, inches = 0):
    """Converts a length from feet and inches to centimeters"""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm


print(cm(feet = 5))
print(cm(inches = 10))
print(cm(feet = 5, inches = 10))

# Types of arguments in functions are: Keyword (feet = 0, inches = 0) and Required (b,h)
# Keyword arguments must come last if both the types are used.


def g(x, y=0):
    return x+y


print(g(5,2))