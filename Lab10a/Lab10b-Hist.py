import matplotlib.pyplot as plt
temp_w_date = []
art = ''
nu = 0
percipitation = []
datafile = open("C:\\Users\\olivi\\PycharmProjects\\Lab01\\ENGR 102 Olivia\\Lab09\\WeatherDataWindows(1).csv", 'r')
temperatures = datafile.readlines()
temperatures.pop(0)
for r in temperatures:
    nu = float(r.split(',')[12])
    percipitation.append(nu)
plt.hist(percipitation)
plt.title("Percipitation Histogram")
plt.xlabel("Levels of Percipitation")
plt.ylabel()
plt.show()
datafile.close()

