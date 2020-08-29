###Create a global Variable For text file
##Possibly Call other programs?
####True/False if 1 or two columns
###2 Arrays if 2 columns
##CONSTANTS = UPPERCASE
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


# def Min(li,li2):
#    li.sort()
#    return li[0]


# def Max(lt,lt2):
#    lt.sort()
#    return lt[-1]
def returner(nam):
    List_1 = []
    List_2 = []
    if type(nam) == tuple:
        Lot1, Lot2 = nam
        Lot1 = sorting(Lot1)  # Sort function from beginning to avoid repetition
        Lot2 = sorting(Lot2)
    else:
        input_fi = open(nam, 'r')
        stu = input_fi.readline().split(',')
        for a in range(len(stu),2):
            List_1 += [1,int(stu[a]),2]
        for b in range(len(stu),):
            List_2 += [int(stu[b])]
        input_fi.close()
        return List_2,List_1


