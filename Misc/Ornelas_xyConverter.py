# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Olivia Ornelas
# Section: 514
# Assignment: CFU 6
# Date: 19 November 2018
from math import sqrt, atan, cos, sin

x = 0
y = 0
r = 0
th = 0


def cart(xi, yi):  # Read in Cartesian
    rad = sqrt((xi ** 2) + (yi ** 2))
    thet = atan(yi / xi)
    return rad, thet


def pol(ri,thi):        #Reads in Polar
    xval = ri*cos(thi)
    yval = ri*sin(thi)
    return xval, yval


choice = int(input("Are you entering polar coordinates or cartesian coordinates? (1 for polar, 2 for cartesian) "))
if choice == 1:
    r = float(input("Enter the radius value of your polar coordinate: "))
    th = int(input("Enter the theta value of your polar coordinate: "))         ##Acount for entering pi by keeping th as a string, and checking to see if pi is in the variable. if it is, turn it a float and use the math.pi / by the number in it ex: pi/4
    retp = pol(r,th)                        ###Value of function return                 pi/4
    print("Your original coordinate was ("+str(r)+", "+str(th)+") in the polar form, and", retp, "in the cartesian form")
if choice == 2:
    x = float(input("Enter the x value of your cartesian coordinate: "))
    y = float(input("Enter the y value of your cartesian coordinate: "))
    retc = cart(x,y)
    print("Your original coordinate was ("+str(x)+", "+str(y)+") in the cartesian form, and", retc, "in the polar form")
