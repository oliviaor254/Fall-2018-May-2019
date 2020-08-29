# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Olivia Ornelas
# Section: 514
# Assignment: Lab 1b-1
# Date: 2 September 2018
from math import *
print(" ")
print("1. This shows the evaluation of f(x)=sin(x)/x, evaluated close to x=1")
print("My guess is 1/2")
x = 1

print(sin(x)/x)
x += 10**-1
print(sin(x)/x)
x = 1+10**-2
print(sin(x)/x)
x = 1+10**-3
print(sin(x)/x)
x = 1+10**-4
print(sin(x)/x)
x = 1+10**-5
print(sin(x)/x)
x = 1+10**-6
print(sin(x)/x)
x = 1+10**-7
print(sin(x)/x)
print(" ")
print("2. This shows the evaluation of g(x)=1-cos(y)/y^2, evaluated close to y=1")
print("My guess is 2")
y = 1
print(1-cos(y)/pow(y, 2))
y += 10**-1
print(1-cos(y)/pow(y, 2))
y = 1+10**-2
print(1-cos(y)/pow(y, 2))
y = 1+10**-3
print(1-cos(y)/pow(y, 2))
y = 1+10**-4
print(1-cos(y)/pow(y, 2))
y = 1+10**-5
print(1-cos(y)/pow(y, 2))
y = 1+10**-6
print(1-cos(y)/pow(y, 2))
y = 1+10**-7
print(1-cos(y)/pow(y, 2))
print(" ")
print("3. This shows the evaluation of h(z)=(1+1/z)^z, evaluated close to z=1")
print("My guess is 10.5")
z = 1
print((1+1/z)**z)
z *= 10
print((1+1/z)**z)
z *= 10
print((1+1/z)**z)
z *= 10
print((1+1/z)**z)
z *= 10
print((1+1/z)**z)
z *= 10
print((1+1/z)**z)
z *= 10
print((1+1/z)**z)

print(z)

