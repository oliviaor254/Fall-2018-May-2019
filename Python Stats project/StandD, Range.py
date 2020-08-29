###Create a global Variable For text file
##Possibly Call other programs?
####True/False if 1 or two columns
###2 Arrays if 2 columns
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def Range(Lst):
    Max = Lst[1]
    Mini = Lst[-1]
    for a in Lst:
            if a > Max:
                Max = a
            if a < Mini:
                Mini = a
    Rg = Max-Mini
    Ran = format(Rg, '.2f')
    return Ran


def Aver(L,L2):
    tot = 0
    count = 0
    try:
        for a in range(len(L)):
            tot += L[a]+ L2[a]
            count += len(L)+len(L2)
        tot /= count
    except:
        for a in range(len(L)):
            tot += L[a]
            count += a
        tot /= count
    return tot

def StndDev(List,List2):
    STD = []
    try:
        acut = Aver(List,List2)
        for b in List:
            std = (b-acut)**2
            STD += [std]
        standard = Aver(STD)
        StDv = sqrt(standard)
        Stand = format(StDv, '.2f')
    except:
        acut = Aver(List)
        for b in List:
            std = (b-acut)**2
            STD += [std]
        standard = Aver(STD)
        StDv = sqrt(standard)
        Stand = format(StDv, '.2f')
    return Stand


Lt = [3, 2, 6, 8, 1, 9, 12]
Lt2 = [5, 7, 10, 3, 26, 18]
print(StndDev(Lt, Lt2))
print(Range(Lt))
print(Range(Lt2))


