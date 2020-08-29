# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Olivia Ornelas
# Section: 514
# Assignment: Lab 09b-3
# Date: 30 October 2018
from math import pow
temperatures = []
max = 0
temp1 = 0
dates = []
min = pow(10, 27)
rain = 0
dailypercip = 0
area = []
counter = 0
hum = 0
hum_percent = 0
art = ''
datafile = open("WeatherDataWindows(1).csv", 'r')
temperatures = datafile.readlines()
temperatures.pop(0)
for bc in temperatures:
    dates.append(bc)
print(dates)
for ac in temperatures:
    art = ac[9:-1]
    area.append(art)
max1 = area[1].split(',')[1]
min1 = area[1].split(',')[3]
print(area)
for a in area:
    if float(a.split(',')[1]) > max: #Find Max
        max = float(a.split(',')[1])
    if float(a.split(',')[3]) < min:        #Find Min
        min = float(a.split(',')[3])
    dailypercip += float(a.split(',')[-1])
    counter += 1
    if float(a.split(',')[-6]) >= 80:       # When average humidity is above 80
                hum += 1
#AVERAGE in July
for b in dates:
    if '7/' in b.split(',')[0]:
        temp1 += float(b.split(',')[2])
temp1 /= counter
print("The average high temperature for July is", temp1)
hum_percent = (hum/counter)*100
rain = dailypercip/counter
print("The percent of days where the humidity was above 80% over the past 3 years is", hum_percent, "%")     #Format
print("The average rain over three years is "+str(rain)+"in.")
print("The maximum temperature is", max)
print("The minimum temperature is ", min)

datafile.close()