# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Olivia Ornelas
# Section: 514
# Assignment: Lab 12b
# Date: 20 November 2018
from turtle import *
import time
stick_num = int(input("Enter the number of tally marks you want to create "))
posis = 0


def getnumbers(stick_amnt=1):

    times = stick_amnt//5       #correct
    '''Enters in the number of tally marks you want to get. Returns the number divided by 5'''
    return times

def getremainder(st=1,t=0):
    remain = st - (t*5)
    '''Takes the number of desired tally marks divided by 5 and the total amount. Returns the remainder from this answer'''
    return remain


def tall(pit, ap=1):        #Creates 1 line at a time
    pit.penup()
    pit.left(90)
    pit.pendown()
    pit.forward(100 + ap)
    pit.penup()
    pit.left(90)
    pit.forward((ap * 5) + (ap * 5))
    '''Creates 1 vertical line at a time'''


def curvature(pl,str=50,stp=0):
    pl.setx(str)
    pl.sety(stp)
    '''Meant to draw diagonal lines (Be called after a bundle is created'''


def turt(p,po=0):
    p.hideturtle()
    for a in range(1, 5):
        tall(p, a)
    p.goto(5*po, 0)
    '''Creates bundles of 4 sticks'''


def leFt(posis, ltvr=0):
    posis = 0
    for l in range(1, ltvr + 1):  # Print leftover sticks
        posis += 10
        tall(pn, l)
        pn.goto(posis, 0)
        pn.down()
    '''Prints out the remainder sticks(With the loop)'''

def bundle(mrk=0):
    posis = 0
    for b in range(mrk):  # Print bundle of sticks
        posis += 10
        turt(pn, posis)
        pn.down()
    '''Draws out the bundles of four tallys'''


sticks = getnumbers(stick_num)

pn = Turtle()
pn.screen.screensize(50, 100)
leftover = getremainder(stick_num, sticks)
bundle(sticks)
leFt(posis, leftover)
done()
