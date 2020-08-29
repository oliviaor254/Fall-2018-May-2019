# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Olivia Ornelas
# Section: 514
# Assignment: CFU 2
# Date: 01 October 2018
import numpy
from math import *
Exam = int(input("Enter grade for exams: "))
Hw = int(input("Enter grade for Homework: "))
Proj = input("Did you do the outside project?(y or n) ")
Hwg = Hw*.40
Exg = Exam*.60
grade = Hwg+Exg         #Check in python Console
if Proj == 'y':
    grade += 5
    if 90 <= grade <= 105:       #Grade can be higher than 100, due to +5 pts from grade
        print("Your grade in the class is an A.")
    if 80 <= grade < 90:                        #Check in python console
        print("Your grade in the class is a B.")
    if 70 <= grade < 80:
        print("Your grade in the class is a C.")
    if 60 <= grade < 70:
        print("Your grade in the class is a D.")
    if grade < 60:
        print("Your grade in the class is an F.")
if Proj == 'n':
    if 80 <= grade <= 100:               #Grade can't B if project was not done
        print("Your grade in the class is a B.")
    if 70 <= grade < 80:
        print("Your grade in the class is a C.")
    if 60 <= grade < 70:
        print("Your grade in the class is a D.")
    if grade < 60:
        print("Your grade in the class is an F.")
