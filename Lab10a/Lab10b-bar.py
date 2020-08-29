#FINISHED
import matplotlib.pyplot as plt
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
Min = []
Max = []
months = []
months_2 = ["January",'February','March','April','May',"June","July",'August','September','October','November', 'December']
dates = []      #dates for x ticks
temp_w_date = []
pressures = []
art = ''
datafile = open("C:\\Users\\olivi\\PycharmProjects\\Lab01\\ENGR 102 Olivia\\Lab09\\WeatherDataWindows(1).csv", 'r')
temperatures = datafile.readlines()
temperatures.pop(0)
for ac in temperatures:
    art = ac[0:-1]
    temp_w_date.append(art)
###### BAR GRAPH#####
for a in temp_w_date:
    if a.split('/')[0] == '1':
        Jan.append(float(a.split(',')[2]))
    elif a.split('/')[0] == '2':
        Feb.append(float(a.split(',')[2]))
    elif a.split('/')[0] == '3':
        Mar.append(float(a.split(',')[2]))
    elif a.split('/')[0] == '4':
        Apr.append(float(a.split(',')[2]))
    elif a.split('/')[0] == '5':
        May.append(float(a.split(',')[2]))
    elif a.split('/')[0] == '6':
        June.append(float(a.split(',')[2]))
    elif a.split('/')[0] == '7':
        July.append(float(a.split(',')[2]))
    elif a.split('/')[0] == '8':
        Aug.append(float(a.split(',')[2]))
    elif a.split('/')[0] == '9':
        Sep.append(float(a.split(',')[2]))
    elif a.split('/')[0] == '10':
        Oct.append(float(a.split(',')[2]))
    elif a.split('/')[0] == '11':
        Nov.append(float(a.split(',')[2]))
    elif a.split('/')[0] == '12':
        Dec.append(float(a.split(',')[2]))
Max.append(max(Jan))
Max.append(max(Feb))
Max.append(max(Mar))
Max.append(max(Apr))
Max.append(max(May))
Max.append(max(June))
Max.append(max(July))
Max.append(max(Aug))
Max.append(max(Sep))
Max.append(max(Oct))
Max.append(max(Nov))
Max.append(max(Dec))
Min.append(min(Jan))
Min.append(min(Feb))
Min.append(min(Mar))
Min.append(min(Apr))
Min.append(min(May))
Min.append(min(June))
Min.append(min(July))
Min.append(min(Aug))
Min.append(min(Sep))
Min.append(min(Oct))
Min.append(min(Nov))
Min.append(min(Dec))
months.append(sum(Jan)/len(Jan))
months.append(sum(Feb)/len(Feb))
months.append(sum(Mar)/len(Mar))
months.append(sum(Apr)/len(Apr))
months.append(sum(May)/len(May))
months.append(sum(June)/len(June))
months.append(sum(July)/len(July))
months.append(sum(Aug)/len(Aug))
months.append(sum(Sep)/len(Sep))
months.append(sum(Oct)/len(Oct))
months.append(sum(Nov)/len(Nov))
months.append(sum(Dec)/len(Dec))
plt.figure(2, figsize=(13, 7))
plt.bar(months_2,months, yerr=stdev(June),capsize=7) #Might need to use max/min and error bars
plt.plot(months_2,Min,'ro')
plt.plot(months_2,Max,'ro')
plt.title("Bar Graph: Average Temperature")
plt.xlabel("Months")
plt.ylabel("Temperatures")
plt.show()
datafile.close()