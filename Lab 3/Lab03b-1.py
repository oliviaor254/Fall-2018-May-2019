# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Olivia Ornelas
# Section: 514
# Assignment: Lab 2b-2
# Date: 12 September 2018
from math import*
print('1a. Enter mass and volume to determine Kinetic Energy:')
mass = float(input('Mass:'))
Vol = float(input('Volume:'))
kin = mass*pow(Vol, 2)        #Kinetic Energy formula
print("Kinetic Enrgy: ",kin, "J")
print("1b. Enter Normal stress, Angle of internal fraction, and its cohesion:")
Nstress = float(input("Normal Stress:"))
Cohes = float(input("Cohesion:"))
AngofInternalFrict = float(input("Angle of Internal Friction:"))
mh = Nstress+Cohes*tan(degrees(AngofInternalFrict))  # Mohr failure criterion
print(mh,"Shear Strength (Based off Mohr-Failure Criterion")
print("1c. Enter Number of Days, the initial production rate, decline rate, and Hyperbolic constant.")
Days = float(input("Number of Days: "))
ProRate = float(input("Initial Production Rate: "))
DeclRate = float(input("Decline Rate: "))
HypC = float(input("Hyperbolic Constant: "))
arp_e = 1+HypC*DeclRate*Days**(1/HypC)
arp_eq = ProRate/arp_e
print("Flowrate of", arp_eq, "Cubic feet per day (in thousands)")
print("1d. Enter the arrival and service rates for an M/M/1 Queue to determine the average length.")
Arate = float(input("Arrival rate:"))
Serv = float(input("Service rate:"))
p = Arate/Serv                # M/M/1 Queue
q = pow(p, 2)/1-p
print("Average length of M/M/1 Queue", q, "Customers per service")
