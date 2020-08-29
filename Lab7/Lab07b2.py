#Finished Bitch
import numpy
from math import*
vctr_amnt = int(input('How many dimensions does this vector have? '))
strA = input('Enter components for Vector A (x,y,z,etc): ')
vecA = list(map(int, strA.split(',')))
strB = input('Enter components for Vector B (x,y,z,etc): ')
vecB = list(map(int, strB.split(',')))
rvec = []
dotpr = 0
rvec2 = []
sqrtp = 0
print(vecB)
print(vecA)
for xo in range(len(vecA)):
    rvec.append(vecA[xo]+vecB[xo])
    rvec2.append(vecA[xo] - vecB[xo])
    dotpr += (vecA[xo]*vecB[xo])
    sqrtp += (vecA[xo]-vecB[xo])**2
mag = sqrt(sqrtp)
print("Result of A + B:", rvec)
print("Result of A-B:", rvec2)
print("Result of Dot Product between A & B:", dotpr)
print("Result of Magnitude between A & B:", mag)
