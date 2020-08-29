# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Olivia Ornelas
# Section: 514
# Assignment: Lab 2b-1
# Date: 5 September 2018
from math import *
print("Olivia Ornelas, UIN: 827003841, Section 514")
print("Interesting fact: I've been to most parts of Jamaica.")
resistance = 20
current = 5
voltage = 5*20
print(voltage)
mass = 100
velocity = 21
KE = 1/((2*mass)*pow(velocity,2))
print(KE)
fvel = 100
kin_visc = 1.2
char_visc = 2.5
Reynold_num = (fvel/kin_visc)*char_visc
print(Reynold_num)
Temp = 2200
StefBolt = 5.67e-8
Radiated_E = pow(Temp,4)*StefBolt
print(Radiated_E)
q_i = 100
b = .8
d1 = 2
time = 20
Arps_Equt = q_i/((1+b*d1*time)*1/b)
print(Arps_Equt)
rate_arrived = 20
rate_served = 35
avg_people = rate_arrived/rate_served
avg_length = pow(avg_people, 2)/(1-avg_people)
print(avg_length)
Norm_stress = 20
cohes = 2
Ang_inter_frict = 35
mcfailcrit = cohes + Norm_stress * tan(degrees(Ang_inter_frict))
print(mcfailcrit)
wavelength = 7.5e-7
lattic_spac = 1e-6
MaxDifract = asin(wavelength/2*lattic_spac)
print(MaxDifract)


