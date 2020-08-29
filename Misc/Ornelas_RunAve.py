# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Olivia Ornelas
# Section: 514
# Assignment: CFU 4
# Date: 19 November 2018
Avg_temp = 0
inputfile = open("Temperature.txt", 'r')
outputfile = open("RunningAverages.txt", 'w')  #Opens file to be written into
origtemps = inputfile.readlines()           ##Reads temperatures from the file into a list
length = len(origtemps)/2 +1
if len(origtemps) < 7:          ##Checks if there is enough temperature values
    print("There is not enough data in the file to find the daily values.")
elif len(origtemps) > 7:
    for a in range(1,int(length)):
        Avg_temp = 0
        for b in range(6+a):        ##Increments by one at end and at top?
            Avg_temp += int(origtemps[b][0:1])
        Avg_temp /= 7
        outputfile.write(str(Avg_temp))
        outputfile.write('\n')





inputfile.close()
outputfile.close()
