# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Olivia Ornelas
# Evangelina Cruz
# Ryan Raiford
# Angela Tang
# Sandra Ponce
# Section: 514
# Assignment: Lab 1a-2
# Date: 12 September 2018
from math import *
print("How many pounds to convert to Newtons?")     #A
lbs = float(input())
newton = 4.44822
print(lbs*newton, "Newtons")
print('How many British Thermal Units (BTU) to convert to Joules?')      #B
BTU = float(input())
J = 1055.06
print(BTU*J, "Joules")
print("How many pascals to convert into millimeters of Mercury?")   #C
lbN = float(input())
mmMerc = lbN*(7.5e-3)
print(mmMerc, 'Milimeters of Mercury')
print("How many seconds per revolution to Hertz?")      #D
spr = float(input())
print(spr, "Hertz")
print("How many Miles per Hour to convert to Meters per Second")        #E
MpH = float(input())
mpS = 1609.34/3600
print(MpH*mpS, 'Meters per second')
print("Enter Farenheit value:")                     #F
Faren = float(input())
Cel = (5/9)*(Faren-32)
print(Cel, "Celsisus")
print("Magnitude of Earthquake 1 (Based off of Richter scale):")                #G
E1 = float(input())
print("Magnitude of Earthquake 2 (Based off of Richter scale):")
E2 = float(input())
Mag = E1-E2
print(10**(4.4+1.5*Mag), 'Joules')

print("How much Voltage to convert to Voltage level")   #H
Volt = float(input())
print('Voltage Level (dBV):', 20*log10(Volt))



