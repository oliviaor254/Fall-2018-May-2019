# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Olivia Ornelas
# Section: 514
# Assignment: Lab 3b-2
# Date: 16 September 2018
from math import*
import numpy
observ_x = float(input("Enter position of observer (x-value) "))
observ_y = float(input("Enter position of observer (y-value) "))
observ_z = float(input("Enter position of observer (z-value) "))
Observer1 = [observ_x,observ_y,observ_z]
x1 = float(input("Enter position of first observed point (x-value) "))
y1 = float(input("Enter position of first observed point (y-value) "))
z1 = float(input("Enter position of first observed point (z-value) "))

x2 = float(input("Enter position of second observed point (x-value) "))
y2 = float(input("Enter position of second observed point (y-value) "))
z2 = float(input("Enter position of second observed point (z-value) "))

v1x = x1-observ_x
v1y = y1-observ_y
v1z = z1-observ_z
v2x = x2-observ_x
v2y = y2-observ_y
v2z = z2-observ_z
vect1 = [v1x, v1y, v1z]
vect2 = [v2x, v2y, v2z]
dotprod = (v1x*v2x)+(v1y*v2y)+(v1z*v2z)
magvec1 = sqrt((v1x**2)+(v1y**2)+(v1z**2))
magvec2 = sqrt((v2x**2)+(v2y**2)+(v2z**2))
angle = degrees(acos(dotprod/(magvec1*magvec2)))

print("point of observer is", Observer1)
print("Vector from observer to first point", vect1)
print("Vector from observer to second point", vect2)
print("angle between the two vectors is", angle)
