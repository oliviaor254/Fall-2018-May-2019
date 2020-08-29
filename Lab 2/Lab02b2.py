# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Olivia Ornelas
# Section: 514
# Assignment: Lab 2b-2
# Date: 10 September 2018
Time1 = 13
Time2 = 84
Time3 = 50
X1 = 1
X2 = 23
mx1 = (X1-X2)/(Time1-Time2)
bx1 = X1-mx1*Time1
X3 = (mx1*Time3)+bx1

Y1 = 3
Y2 = -5
my1 = (Y1-Y2)/(Time1-Time2)
by1 = Y1-(my1*Time1)
Y3 = (my1*Time3)+by1

Z1 = 7
Z2 = 10
mz1 = (Z1-Z2)/(Time1-Time2)
bz1 = Z1-(mz1*Time1)
Z3 = mz1*Time3+bz1
print("The position at time 50 is (", X3, ",", Y3, ",", Z3, ")")
