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
# Assignment: Lab 10a-2
# Date: 31 October 2018
import matplotlib.pyplot as plt
from math import pi
import numpy as np
#Bar Graph of how many people own each type of pet
pets = ['Cats', 'Fish', 'Dogs']
number_of_pets = [15,5,28]
plt.bar(pets,number_of_pets)
plt.xlabel('Types of Pets')
plt.ylabel('Amount of pets owned')
plt.suptitle('Type of Pets owned')
plt.show()
#Graph of exponential
x = np.linspace(0,(4*pi)/3,100)
y = np.exp(x)
plt.plot(x,y)
plt.show()
#D = np.array([4,5,6],[8,9,10],[12,3,23])