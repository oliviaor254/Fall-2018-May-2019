import numpy as np
import matplotlib.pyplot as plt

months_2 = ["January",'February','March','April','May',"June","July",'August','September','October','November', 'December']
max = 0
temp1 = 0
dates = []      #dates for x ticks
min = pow(10, 27)
rain = 0
dailypercip = 0
avg_temps = []
temp_w_date = []
dwpnt = []
pressures = []
art = ''
datafile = open("C:\\Users\\olivi\\PycharmProjects\\Lab01\\ENGR 102 Olivia\\Lab09\\WeatherDataWindows(1).csv", 'r')
temperatures = datafile.readlines()
temperatures.pop(0)
for ac in temperatures:
    art = ac[0:-1]  #Puts values from file into list of temp values
    temp_w_date.append(art)
for g in temp_w_date:
    tp = float(g.split(',')[2])
    dp = float(g.split(',')[5])
    avg_temps.append(tp)
    dwpnt.append(dp)
plt.scatter(avg_temps,dwpnt, s=(np.pi*3), c=(0,0,0), alpha=0.5)
plt.title("Scatter Plot: Average Temperature vs. Average Dew Point")
plt.xlabel("Average Temperature")
plt.ylabel("Average Dew Point")
plt.show()
datafile.close()
