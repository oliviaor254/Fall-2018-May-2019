import matplotlib.pyplot as plt
import numpy as np
##Histogram


def plothist(Li, l):
    Li = np.asarray(Li)
    l = np.asarray(l)
    try:
        plt.hist(Li)
#        plt.savefig("Histogram for column 1.jpeg")
        plt.hist(l)
#        plt.savefig("Histogram for column 2.jpeg")
    except IndexError:
        plt.hist(Li)
#        plt.savefig("Histogram for Column 1.jpeg")


def plotplts(L, Li):    #
    L = np.asarray(L)
    Fig = plt.figure()
    plt1 = Fig.add_subplot(4, 2, 1)
    plt2 = Fig.add_subplot(4, 2, 2)
    plt3 = Fig.add_subplot(4, 2, 3)
    plt4 = Fig.add_subplot(4, 2, 4)
    plt1.semilogx(L, np.sin(2*np.pi*L))
    plt1.grid(True)
    plt1.set_title("Semi-Log X Graph")
    plt1.set_ylabel("Y")
    plt1.set_xlabel("X")
    plt2.semilogy(L, np.exp(-L/5.0))
    plt2.grid(True)
    plt2.set_title("Semi-Log Y Graph")
    plt3.loglog(L, 20*np.exp(-L/10.0), basex=2)
    plt3.grid(True)
    plt3.set_title("Log-Log Graph")
    plt4.plot(L)
    plt4.set_title("Linear Graph")
#    Fig.savefig("Subplots of Everything.jpeg")
    plt.show()


kist = [2, 4, 6, 8, 10, 12, 14, 16]
jist = [1, 3, 5, 7, 9, 11, 13, 14, 15]
plotplts(kist, jist)
plothist(kist, jist)
