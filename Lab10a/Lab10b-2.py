# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Olivia Ornelas
# Section: 514
# Assignment: Lab 10b-1
# Date: 30 October 2018
#All variable names are after cast members of the MATRIX
import numpy as nip
import matplotlib.pyplot as plt
from math import pow
from statistics import stdev
Jan = []
Feb = []
Mar = []
Apr = []
May = []
June = []
July = []
Aug = []
Sep = []
Oct = []
Nov = []
Dec = []
months = []
months_2 = ["January",'February','March','April','May',"June","July",'August','September','October','November', 'December']
temp1 = 0
dates = []      #dates for x ticks
rain = 0
dailypercip = 0
temps = []

temp_w_date = []
pressures = []
art = ''
datafile = open("C:\\Users\\olivi\\PycharmProjects\\Lab01\\ENGR 102 Olivia\\Lab09\\WeatherDataWindows(1).csv", 'r')
temperatures = datafile.readlines()
temperatures.pop(0)
for ac in temperatures:
    art = ac[0:-1]  #Puts values from file into list of temp values
    temp_w_date.append(art)        #Sub labels (Has dates
for a in temp_w_date:
        dates.append(a.split(',')[0])
        avg_val = float(a.split(',')[2])        #Averages
        pressures.append(float(a.split(',')[-3]))
        temps.append(avg_val)
dates = nip.asarray(dates)
fig,ax1 = plt.subplots()

ax1.set_ylabel('Pressure', color='tab:green')
ax1.set_xlabel("Number of Days from Jan. 2015")
ax1.plot(dates,pressures, color='g')
ax1.tick_params(axis='y',labelcolor='g')

ax2 = ax1.twinx()

ax2.set_ylabel("Temperature", color='tab:blue')
ax2.plot(dates,temps, color='tab:blue')
ax2.tick_params(axis='y', labelcolor='blue')
fig.tight_layout()
plt.show()
datafile.close()
