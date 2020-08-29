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
# Assignment: Python Statistics Project
# Date: 2 December 2018
######################
from math import sqrt
import datetime
import numpy as np
import matplotlib.pyplot as plt
choice = ''
CONTPROG = True
USERNAME = ''
OUTPUTFILE = ''
NOW = datetime.datetime.now()
def sorting(L):
    ''' L = {A list}
    Function is designed to read in a list, L, and return the sorted (bubble) version of it. '''
    for val in range(len(L) - 1, 0, -1):
        maxpos = 0
        for sort_ in range(val + 1):
            if L[sort_] > L[maxpos]:
                maxpos = sort_
        temp = L[val]
        L[val] = L[maxpos]
        L[maxpos] = temp
    return L


def EnterData():
    ''' Function designed to be called and gather the name of the file chosen to be read, or Allows the user to manually enter data.
    If data is in a file, returns the name of the file. If the data is manually inputted, the List is returned in tuple form.'''
    listot2 = []
    listot = []
    style = input("Do you want to read the data from a file? (Y or N): ")
    if style == "Y":
        name = input("What is the name of the file? (Include extensions such as .csv, .tsv, .dat, .txt) ")
        return name
    else:
        otinput = input("Enter the data from column 1 (Separate by commas): ")
        lis = otinput.split(',')
        for nu in lis:
            listot += [int(nu)]
        ot2 = input("Is there a second column of data (Y or N)? ")
        if ot2 == 'Y':
            otinput2 = input("Enter the data from column 2 (Separate by commas): ")
            lis2 = otinput2.split(",")
            for num in lis2:
                listot2 += [int(num)]

            return listot, listot2
        elif ot2 == 'N':
            return listot, listot2


def returner(nam):
    ''' nam: either a tuple or str. If tuple, separates it into 2 more lists and returns them.
    If nam is a string, the function reads data from the file and placed into List_1,List_2 depending on the number of columns.
    The data is separated according to if it is a .csv,.tsv or .dat/.txt.'''
    List_1 = []
    List_2 = []
    if type(nam) == tuple:
        List_1, List_2 = nam
    else:
        input_fi = open(nam, 'r')
        if input_fi[-4:] == '.csv':
            stu = input_fi.readline().split(',')
        elif input_fi[-4:] == '.tsv':
            stu = input_fi.readline().split('\t')
        else:
            stu = input_fi.readline().split('\n')
        for a in range(len(stu),2):
            List_1 += [1,int(stu[a]),2]
        for b in range(len(stu),):
            List_2 += [int(stu[b])]
        input_fi.close()
    List_1 = sorting(List_1)  # Sort function from beginning to avoid repetition
    List_2 = sorting(List_2)
    return List_2, List_1


def usern():
    '''Returns a str that is the username that the user chooses.'''
    use = input("Please enter the username you would like to use for this software: ")
    return use


def outp():
    '''Returns a str that is the name of the output file that the user chooses. This includes the file type.'''
    print("Enter the name of the output file you want to use. Include file type(for example: Name.txt,Name.csv, etc.)")
    output = input("If the file exists, it will be replaced. ")     # HANDLE IF NO EXTENSION?
    while output[-4:] != '.csv' or output[-4:] != '.tsv' or output[-4:] != '.txt' or output[-4:] != '.dat':
        output = input("That is not an acceptable file. Please enter a .tsv, .csv, .dat, or .txt: ")
    return output


def Min(li):    # li2=[]
    ''' li,li2=[]: 1 or 2 lists.
    Finds the minimum by calling the first element because the list is presorted. See _____().'''
    return li[0]


def m_ax(lt):
    '''lt: List
    Finds the maximum by calling the first element because the list is presorted. See _____().'''
    max_ = int(lt[-1])  # FIX!!
    return max_


def Avg(L):
    '''L: 1 or 2 lists.
    Calculates and returns the Average of List 1 & List 2 (If applicable).'''
    tot = 0
    count = 0
    for a in range(len(L)):
            tot += L[a]
            count += len(L)
    tot /= count
    return tot


def var_iance(x):
    '''x: List
    Calculates and returns the variance of a list.'''
    avg = Avg(x)
    y = 0
    for i in x:
        y += i-avg
    y /= len(x)
    return y


def rnge(lis_1):
    '''lis_1: List.
    Calculates and returns the Range of a list. Function is presorted by _____()'''
    Max = lis_1[-1]
    Mini = lis_1[0]
    Rg = Max - Mini
    return Rg


def StndDev(List):
    '''List,List2: Lists
    Calculates and returns the standard deviation of 2 lists (if applicable).'''
    STDV = []
    acut = Avg(List)
    for b in List:
        std = (b-acut)**2
        STDV += [std]
    standard = Avg(STDV)
    StDv = sqrt(standard)
    return StDv


def Med_ian(A):
    '''A: List
    Calculates and returns the median of the list. List presorted by _____() in line ___ of the software.'''
    if len(A)%2 == 0:
        Med = (A[int(len(A)/2)] + A[int((len(A)/2))])/2
    else:
        Med = A[int(len(A)/2)]
    return Med


def MoDe(L):
    ''' L: List
    Calculates and returns the mode of the parameter.'''
    Mode = 0
    spot = 0
    for n in range(len(L)):
        ct = L.count(L[n])
        if ct > Mode:
            Mode = ct
            spot = n
    return L[spot]


def Basic_stats(l1, l2=[]):
    '''l1,l2=[]: List
    Formats all of the Statistic calculations of the software. When called, the values are presented.'''
    try:
        mx = format(m_ax(l1), '.2f')
        print("Maximum for Column 1 Data:"+str(mx))
        mx2 = format(m_ax(l2),'.2f')
        print("Maximum for Column 2 Data:"+str(mx2))
    except IndexError:
        mx = format(m_ax(l1), '.2f')
        print("Maximum for Column 1 Data:" + str(mx))
    try:
        Mn = format(Min(l1), '.2f')
        print("Minimum for Column 1 Data:"+str(Mn))
        Mn2 = format(Min(l2), '.2f')
        print("Minimum for Column 2 Data:"+str(Mn2))
    except IndexError:
        Mn = format(Min(l1), '.2f')
        print("Minimum for Column 1 Data:"+str(Mn))
    try:
        Ag = format(Avg(l1), '.2f')
        print("Average for Column 1 Data:"+str(Ag))
        Ag2 = format(Avg(l2), '.2f')
        print("Average for Column 2 Data:"+str(Ag2))
    except ZeroDivisionError:
        Ag = format(Avg(l1),'.2f')
        print("Average for Column 1 Data:"+str(Ag))
    try:
        Rnge = format(rnge(l1), '.2f')
        print("Range for Column 1 Data:"+str(Rnge))
        Rnge2 = format(rnge(l2), '.2f')
        print("Range for Column 2 Data:"+str(Rnge2))
    except IndexError:
        Rnge = format(rnge(l1), '.2f')
        print("Range for Column 1 Data:"+str(Rnge))
    Stde = format(StndDev(l1), '.2f')
    print("Standard Deviation for Column 1 Data:"+str(Stde))
    try:
        meDiaN = format(Med_ian(l1), '.2f')
        print("Median for Column 1 Data:"+str(meDiaN))
        meDian2 = format(Med_ian(l2), '.2f')
        print("Median for Column 2 Data:"+str(meDian2))
    except IndexError:
        meDiaN = format(Med_ian(l1), '.2f')
        print("Median for Column 1 Data:"+str(meDiaN))
    try:
        VArs = format(var_iance(l1), '.2f')
        print("Variance for Column 1 Data:"+str(VArs))
        VarS2 = format(var_iance(l2), '.2f')
        print("Variance for Column 2 Data:"+str(VarS2))
    except (IndexError, ZeroDivisionError):
        VArs = format(var_iance(l1), '.2f')
        print("Variance for Column 1 Data:"+str(VArs))
    try:
        ModE = format(MoDe(l1), '.2f')
        print("Mode for Column 1 Data:"+str(ModE))
        ModE2 = format(MoDe(l2), '.2f')
        print("Mode for Column 2 Data:"+str(ModE2))
    except IndexError:
        ModE = format(MoDe(l1), '.2f')
        print("Mode for Column 1 Data:"+str(ModE))


def outputfile_write(l1, l2=[]):
    '''l1,l2=[]: Lists
    Creates and writes to the outputfile given previously. Performs the same calculations as Basic_stats(l1,l2).
    writes into the file depending on what the extension is.'''
    of = open(OUTPUTFILE, 'w')
    if OUTPUTFILE[-4:] == '.csv':   # Adjusts the Output of the data depending on what the file name extension is (file name chosen from input)
        of.write(filename + USERNAME + str(NOW) + ',')
        of.write("Column 1 Data:,Maximum:,")
        of.write(format(m_ax(l1), '.2f')+',Minimum:,')
        of.write(format(Min(l1), '.2f')+',Average:,')
        of.write(format(Avg(l1), '.2f')+',Range:,')
        of.write(format(rnge(l1), '.2f')+',Standard Deviation:,')
        of.write(format(StndDev(l1), '.2f')+',Median:,')
        of.write(format(Med_ian(l1), '.2f')+',Variance:,')
        of.write(format(var_iance(l1), '.2f')+',Mode:,')
        of.write(format(MoDe(l1), '.2f')+',Count:,')
        of.write(str(len(l1))+',')
        # Column 2
        of.write("Column 2 Data:,Maximum:,")
        of.write(format(m_ax(l2), '.2f')+',Minimum:,')
        of.write(format(Min(l2), '.2f')+',Average:,')
        of.write(format(Avg(l2), '.2f')+',Range:,')
        of.write(format(rnge(l2), '.2f')+',Standard Deviation:,')
        of.write(format(StndDev(l2), '.2f')+',Median:,')
        of.write(format(Med_ian(l2), '.2f')+',Variance:,')
        of.write(format(var_iance(l2), '.2f')+',Mode:,')
        of.write(format(MoDe(l2), '.2f')+',Count:,')
        of.write(str(len(l2))+',')
    elif OUTPUTFILE[-4:] == '.tsv':
        of.write(filename + USERNAME + str(NOW) + '\t')
        of.write("Column 1 Data\tMaximum\t")
        of.write(format(m_ax(l1), '.2f')+'\tMinimum:\t')
        of.write(format(Min(l1), '.2f')+'\tAverage:\t')
        of.write(format(Avg(l1), '.2f')+'\tRange:\t')
        of.write(format(rnge(l1), '.2f')+'\tStandard Deviation:\t')
        of.write(format(StndDev(l1), '.2f')+'\tMedian:\t')
        of.write(format(Med_ian(l1), '.2f')+'\tVariance:\t')
        of.write(format(var_iance(l1), '.2f')+'\tMode:\t')
        of.write(format(MoDe(l1), '.2f')+'\tCount\t')
        of.write(str(len(l1))+'\t')
        of.write("Column 2 Data\tMaximum\t")
        of.write(format(m_ax(l2), '.2f')+'\tMinimum:\t')
        of.write(format(Min(l2), '.2f')+'\tAverage:\t')
        of.write(format(Avg(l2), '.2f')+'\tRange:\t')
        of.write(format(rnge(l2), '.2f')+'\tStandard Deviation:\t')
        of.write(format(StndDev(l2), '.2f')+'\tMedian:\t')
        of.write(format(Med_ian(l2), '.2f')+'\tVariance:\t')
        of.write(format(var_iance(l2), '.2f')+'\tMode:\t')
        of.write(format(MoDe(l2), '.2f')+'\tCount:\t')
        of.write(str(len(l2))+'\t')
    else:
        of.write(filename + USERNAME + str(NOW) + '\n')
        of.write("Data for column 1 Data\nMaximum:\n")
        of.write(format(m_ax(l1), '.2f')+'\nMinimum:\n')
        of.write(format(Min(l1), '.2f')+'\nAverage:\n')
        of.write(format(Avg(l1), '.2f')+'\nRange:\n')
        of.write(format(rnge(l1), '.2f')+'\nStandard Deviation:\n')
        of.write(format(StndDev(l1), '.2f')+'\nMedian:\n')
        of.write(format(Med_ian(l1), '.2f')+'\nVariance:\n')
        of.write(format(var_iance(l1), '.2f')+'\nMode:\n')
        of.write(format(MoDe(l1), '.2f')+'\n')
        of.write("Data for column 2 Data\nMaximum:\n")
        of.write(format(m_ax(l2), '.2f')+'\nMinimum:\n')
        of.write(format(Min(l2), '.2f')+'\nAverage:\n')
        of.write(format(Avg(l2), '.2f')+'\nRange:\n')
        of.write(format(rnge(l2), '.2f')+'\nStandard Deviation:\n')
        of.write(format(StndDev(l2), '.2f')+'\nMedian:\n')
        of.write(format(Med_ian(l2), '.2f')+'\nVariance:\n')
        of.write(format(var_iance(l2), '.2f')+'\nMode:\n')
        of.write(format(MoDe(l2), '.2f')+'\nCount:\n')
        of.write(str(len(l2))+'\n')
        of.write("Original Data- Column 1: "+l1+" Original Data- Column 2:"+l2)
    of.close()


def Viz_Hist(Li,l=[]):
    '''Li,l=[]: Lists
    Graphs Histograms of the given data, and saves each column of data to a .jpeg (2 separate files).'''
    # Histograms
    Li = np.asarray(Li)
    l = np.asarray(l)
    try:
        plt.hist(Li)
        plt.show()
        YN1 = input("Save data of column 1 as .jpeg (Y or N)? ")        # Repaeat Question for other plots (OPTION 4)
        if YN1 == "Y":
            plt.savefig(USERNAME+'_12/4/2018_Fig_1_.jpeg')      # uSERNAME_NUMBRE
        plt.hist(l)
        plt.show()
        YN = input("Save data of column 2 as .jpeg (Y or N)? ") # HANDLE IF NOT THE WRITE INPUT
        while YN.isdigit() or (YN != 'N' and YN != 'Y'):
            YN = input("That is not the correct format. Please enter Y or N \n Save data of column 2 as .jpeg (Y or N)? ")
            if YN == 'Y':
                plt.savefig(USERNAME+'_12/4/2018_Fig_2_.jpeg')
                continue
            if YN == 'N':
                continue
    except IndexError:
        plt.hist(Li)
        plt.show()
        YN = input("Save data for column 1 as .jpeg (Y or N)? ")
        while YN.isdigit() or (YN != 'N' and YN != 'Y'):
            YN = input("That is not the correct format. Please enter Y or N \n Save data of column 2 as .jpeg (Y or N)? ")
            if YN == 'Y':
                plt.savefig(USERNAME+'_12/4/2018_Fig_1_.jpeg')
                continue
            if YN == 'N':
                continue


def Viz_plots(l_1, li_2=[]):
    '''l_1,li_2=[]: Lists
    Creates graphs of coulmn 1 and 2, respectively, for log-log,linear,semilog-x,and semilog-y.
    Illustrates the graphs on 2 different figures. Saves these 2 figures to .jpegs'''
    # LIST 1        Work on Spacing for graphs
    l_1 = np.asarray(l_1)           # Figure out how to make a title for entire figure
    Fig = plt.figure()
    plt1 = Fig.add_subplot(4, 2, 1)
    plt2 = Fig.add_subplot(4, 2, 2)
    plt3 = Fig.add_subplot(4, 2, 3)
    plt4 = Fig.add_subplot(4, 2, 4)
    plt1.semilogx(l_1, np.sin(2*np.pi*l_1))
    plt1.grid(True)
    plt1.set_title("Semi-Log X Graph")
    plt1.set_xlabel("X")
    plt1.set_ylabel("Y")
    plt2.semilogy(l_1,np.exp(-l_1/5.0))
    plt2.grid(True)
    plt2.set_title("Semi-Log Y Graph")
    plt1.set_xlabel("X")
    plt1.set_ylabel("Y")
    plt3.loglog(l_1, 20*np.exp(-l_1/10.0), basex=2)
    plt3.grid(True)
    plt3.set_title("Log-Log Graph")
    plt1.set_xlabel("X")
    plt1.set_ylabel("Y")
    plt4.plot(l_1)
    plt4.set_title("Linear Graph")
    plt1.set_xlabel("X")
    plt1.set_ylabel("Y")
    plt.show()
    yN = input("Due you want to meet save the data as a .jpeg (Y or N)?")
    while yN.isdigit() or (yN != 'N' and yN != 'Y'):
        if yN == 'Y':
            Fig.savefig(USERNAME+'_12/4/2018_Fig_3_.jpeg')
        if yN == 'N':
            continue
    # List 2
    if len(li_2) > 0:
        li_2 = np.asarray(li_2)
        Fig2 = plt.figure()
        plt2_1 = Fig2.add_subplot(4, 2, 1)
        plt2_2 = Fig2.add_subplot(4, 2, 2)
        plt2_3 = Fig2.add_subplot(4, 2, 3)
        plt2_4 = Fig2.add_subplot(4, 2, 4)
        plt2_1.semilogx(li_2, np.sin(2 * np.pi * li_2))
        plt2_1.grid(True)
        plt2_1.set_title("Semi-Log X Graph")
        plt2_1.set_xlabel("X")
        plt2_1.set_ylabel("Y")
        plt2_2.semilogy(li_2, np.exp(-li_2 / 5.0))
        plt2_2.grid(True)
        plt2_2.set_title("Semi-Log Y Graph")
        plt2_2.set_xlabel("X")
        plt2_2.set_ylabel("Y")
        plt2_3.loglog(li_2, 20 * np.exp(-li_2 / 10.0), basex=2)
        plt2_3.grid(True)
        plt2_3.set_title("Log-Log Graph")
        plt2_3.set_xlabel("X")
        plt2_3.set_ylabel("Y")
        plt2_4.plot(li_2)
        plt2_4.set_title("Linear Graph")
        plt2_4.set_xlabel("X")
        plt2_4.set_ylabel("Y")
        plt.show()
        Yn = input("Do you want to save the data for column 2 to a .jpeg? ")
        while Yn.isdigit() or (Yn != 'N' and Yn != 'Y'):
            Yn = input("That is not the correct format. Please enter Y or N \n Save data of column 2 as .jpeg (Y or N)? ")
            if Yn == 'Y':
                Fig.savefig(USERNAME+'_12/4/2018_Fig_4_.jpeg')
            if Yn == 'N':
                continue


Lot1 = []
Lot2 = []

while CONTPROG:
    print('1. Set Username\n')
    print('2. Set Output File\n')
    print('3.Enter data\n')
    print('4.Display Basic Statistics\n')
    print('5.Visualize Data (As a histogram)\n')
    print('6.Visualize Data (linear, semi-logx, semi-logy, log-log plots)\n')
    print('7. Exit\n')
    # Get user input
    choice = input("Enter a number to choose what to do: ")
    while choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
        choice = input("Sorry! That was not an acceptable choice. Please enter a number 1-5.")

    #  Which action to take based on the user's input
    if choice == '1':
        USERNAME = usern()
    if choice == '2':
        OUTPUTFILE = outp()
    if choice == '3':
        # Call data initialization function for for option 1
        filename = EnterData()
        Lot2, Lot1 = returner(filename)
        Lot1 = sorting(Lot1)
        Lot2 = sorting(Lot2)
    if choice == '4':
        # Call Basic stats functions for for option 2
        Basic_stats(Lot1, Lot2)
        outputfile_write(Lot1, Lot2)
    if choice == '5':
        # Calls Histogram Plot function for for option 3
        Viz_Hist(Lot1, Lot2)
    if choice == '6':
        # Calls SubPlots function for option 4
        Viz_plots(Lot1, Lot2)
    if choice == '7':
        # Change 'while' condition to False in order to exit
        print('Goodbye.\n')
        CONTPROG = False
