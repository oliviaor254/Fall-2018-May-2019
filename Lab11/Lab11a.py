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
# Assignment: Lab 11a-1
# Date: 7 November 2018
x1 = int(input("Enter an x value: "))
g = int(input("Enter a guess for the root (initial"))
xin = int(input("Enter A root Guess"))
rootlist = []
def f(x1):
    (x1**2)-9
    return x1
def deriv(x):
    a = 10
    while(a>10**-6):
        a = (f(x+a)-f(x))/a
    return(a)
def newton_step(xi):

    xii = f(xi)/deriv(xi)
    return xii
def newton(guess):
    rootlist.append(guess)
    rootlist.append(newton(guess))
    while(deriv(abs(guess)-newton(guess))>10**-6):
        rootlist.append(newton_step())
newton(g)
newton_step(xin)
f(x1)