# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Olivia Ornelas
# Section: 514
# Assignment: Lab 4b-2
# Date: 23 September 2018
import numpy
from math import*
strain = float(input("Enter a Strain Value: "))     #Get strain value
ax = .02
ay = 42
bx = .023
by = 42.1
cx = .06
cy = 43
dx = .18
dy = 60
ex = .27
ey = 50
aslope = ay-0/ax-0              #Slopes of eqtns in each section, for the 4 lines
bslope = by-ay/bx-ax
cslope = cy-by/cx-bx
dslope = dy-cy/dx-cx
eslope = ey-dy/ex-dx
if 0<strain<ax:
    aeqtn = (aslope*strain)-(aslope*ax)+ay          #Eqtn for each segment
    print("The stress for a strain of "+str(strain)+" is "+str(aeqtn)+".")
elif ax<strain<bx:
    beqtn = (bslope*strain)-(bslope*bx)+by
    print("The stress for a strain of "+str(strain)+" is "+str(beqtn)+".")
elif bx<strain<cx:
    ceqtn = (cslope*strain)-(cslope*cx)+cy
    print("The stress for a strain of "+str(strain)+" is "+str(ceqtn)+".")
elif cx<strain<dx:
    deqtn = (dslope*strain)-(dslope*dx)+dy
    print("The stress for a strain of "+str(strain)+" is "+str(deqtn)+".")
elif dx<strain<ex:
    Eeqtn = (eslope*strain)-(eslope*ex)+ey
    print("The stress for a strain of "+str(strain)+" is "+str(Eeqtn)+".")
elif strain == ax:
    print("The stress for a strain of "+str(strain)+" is "+str(ay)+".")
elif strain == bx:
    print("The stress for a strain of "+str(strain)+" is "+str(by)+".")
elif strain == cx:
    print("The stress for a strain of "+str(strain)+" is "+str(cy)+".")
elif strain == dx:
    print("The stress for a strain of "+str(strain)+" is "+str(dy)+".")
elif strain == ex:
    print("The stress for a strain of "+str(strain)+" is "+str(ey)+".")
