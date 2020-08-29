# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Olivia Ornelas
# Section: 514
# Assignment: Lab 11b-1
# Date: 10 November 2018
from math import pi
###### Part A###


def box_vol(l,w,h,r):           #CHECK MATH
    vhole = (r**2)*pi*h
    vol_wo_hole = l*w*h
    if r< min(l/2, w/2):
        vol = vol_wo_hole-vhole
    else:
        vol = vhole-vol_wo_hole
    return vol


Blength = float(input("Enter the length of the box: "))
Bheight = float(input("Enter the height of the box: "))
Bwidth = float(input("Enter the width of the box: "))
rhole = float(input("Enter the radius of the hole that has been drilled: "))
print(box_vol(Blength, Bwidth, Bheight, rhole))
######PART B###
listprofit = []


def profit (name, acost, products):
    for a in range(len(name)):
        prof = int(products[a])-int(acost[a])
        listprofit.append(prof)
    return listprofit


def profitability (n, ac, pr):
    actuary = profit(n,ac,pr)
    small = min(profit(n,ac,pr))
    vsmall = actuary.index(small)
    nsmall = n[vsmall]
    return small, nsmall


co_name = input("Enter a list of company names (separate by commas): ")
comp_name = co_name.split(',')
co_ann = input("Enter a list of those company's annual cost (separate by commas): ")
comp_anre = co_ann.split(',')
co_prod = input("Enter a list of those company's value of products produced (separate by commas): ")
comp_prod = co_prod.split(',')
least = profitability(comp_name, comp_anre, comp_prod)      ##RETURNS A TUPLE. NOT RIGHT
print("The company that is least net profitable is", least)
##############PART C##


def label(n, addy, c, s, z, ad2):               #METHOD FIRST {1.Import 2. Method Definitions 3. Main Code
    if ad2 == 'n/a':
        m_label = n + '\n' + addy + '\n' + c + ' ' + s + ' ' + z
    else:
        m_label = n + '\n' + addy + '\n' + ad2 + '\n' + c + ' ' + s + ' ' + z
    return m_label


name = input("Enter the name to be used for the mailing label: ")
address = input("Enter the address to be used for the mailing label: ")
address2 = input("Enter the 2nd address line (n/a if no 2nd line is needed): ")
city = input("Enter the city to be used for the mailing label: ")
state = input("Enter the state to be used for the mailing label: ")
zip = input("Enter the zip code to be used for the mailing label: ")
mail = label(name, address, city, state, zip, address2)
print(mail)
#####PART D###


def readf(f):
    f += '.csv'
    inputfile=open(f, 'r')
    filename2 = f+'.tsv'
    writefile = open(filename2, 'w')
    for b in f:
        for a in range(len(b)):
            if ',' == b[a:a]:
                writefile.write('\t')
            else:
                writefile.write(b[a:a])
    inputfile.close()
    writefile.close()


filename = input("Enter the name of the csv file that you want to read into the program: ")
readf(filename)
######Part E##


def stati(l):
    maximum = 0
    minimum = l[1]
    avg = 0
    for a in l:
        avg += a
        if a > maximum:
            maximum = a
        if a < minimum:
            minimum = a
    avg /= len(l)
    return maximum, minimum, avg


list = input("Enter a list of values (separated by commas): ")
list2 = list.split(',')
print(stati(list2))
####PART F###


def av(l1, l2):
    lst = []
    for a in range(len(l1)-1):
        aver = (l2[a+1]-l2[a])/(l1[a+1]-l1[a])
        lst.append(aver)
    return lst


l = input("Enter the times (separated by commas): ")
list = l.split(',')
li = input("Enter the distances traveled (separated by commas): ")
list2 = li.split(',')
print(av(list, list2))
