# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Olivia Ornelas
# Section: 514
# Assignment: Lab 09b-1
# Date: 30 October 2018
listC = []
listF = []
inputfile = open("Celsius.dat", 'r')
for a in inputfile:
    listC.append(a)
for b in listC:   #Converting C to F multiply 9, divide 5, +32
    CelFer = ((int(b)*9)/5)+32
    listF.append(CelFer)

outputfile = open("Fahrenheit.dat", 'w')
for deg in listF:
    outputfile.write(str(deg)+'\n')      #Edited new text file

inputfile.close()
outputfile.close()