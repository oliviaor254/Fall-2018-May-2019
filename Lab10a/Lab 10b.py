#FINISHED
# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Olivia Ornelas
# Section: 514
# Assignment: Lab 10b-1
# Date: 30 October 2018
#All variable names are after cast members of the MATRIX
import numpy as nump
import matplotlib.pyplot as plt
point = nump.array([(0.0),(1.0)])
print(point)
matrix = nump.array([(1.00583, -0.087156),(0.087156,1.00583)])
carrie_anne = point

for a in range(1,200):
    point = point*matrix
    carrie_anne = nump.append(carrie_anne, point)
    print(point)
hugo = carrie_anne[:200*2:2]    #X values
florence = carrie_anne[1:200*2:2]   #Y values

plt.ylabel("Y values")
plt.xlabel("X Values")
plt.suptitle("Points of matrix multiplied by a point multiplied 155 times.\n Shape/trend of points is a spiral")
plt.plot(hugo, florence)
plt.show()

