#!/bin/python

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, len1, len2):
        self.short_side_length = len1
        self.long_side_length = len2

    def area(self):
        return self.short_side_length * self.long_side_length

    def perimiter(self):
        return 2 * (self.short_side_length + self.long_side_length)

class Circle:
    def __init__(self, rad):
        self.radius = rad

    def area(self):
        return math.pi * (self.radius ** 2)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     q = int(raw_input())
#     queries = []
#     for _ in xrange(q):
#         args = raw_input().split()
#         shape_name, params = args[0], map(int, args[1:])
#         if shape_name == "rectangle":
#             a, b = params[0], params[1]
#             shape = Rectangle(a, b)
#         elif shape_name == "circle":
#             r = params[0]
#             shape = Circle(r)
#         else:
#             raise ValueError("invalid shape type")
#        fptr.write("%.2f\n" % shape.area())

class Vehicle:

    def __init__(self, max, unit):
        self.speed_max = max
        self.speed_units = unit

    def __str__(self):
        return type(self).__name__+" with the maximum speed of "+str(self.speed_max)+" "+self.speed_units

# 2.7 Car(Vehicle, object)
class Car(Vehicle):
    pass

# 2.7 Boat(Vehicle, object)
class Boat(Vehicle):

    def __init__(self, max):
        # 2.7 super(Boat, self)
        super().__init__(max, "knots")


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     q = int(raw_input())
#     queries = []
#     for _ in xrange(q):
#         args = raw_input().split()
#         vehicle_type, params = args[0], args[1:]
#         if vehicle_type == "car":
#             max_speed, speed_unit = int(params[0]), params[1]
#             vehicle = Car(max_speed, speed_unit)
#         elif vehicle_type == "boat":
#             max_speed = int(params[0])
#             vehicle = Boat(max_speed)
#         else:
#             raise ValueError("invalid vehicle type")
#         fptr.write("%s\n" % vehicle)
#     fptr.close()
