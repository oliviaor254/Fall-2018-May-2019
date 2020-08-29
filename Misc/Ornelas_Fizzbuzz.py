# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Olivia Ornelas
# Section: 514
# Assignment: CFU 4
# Date: 17 October 2018
A = int(input("Enter the first positive integer: "))
B = int(input("Enter the second positive integer: "))
uplim = int(input("Enter the upper limit for the game: "))
for count in range(1,uplim+1):  #Goes through limit +1
    if count % A == 0 and count % B == 0: #Check to see if both are true, if so then print fizz buzz
        print('FizzBuzz', end=' ')
    elif count % A == 0:
        print('Fizz', end=' ')
    elif count % B == 0:
        print('Buzz', end=' ')
    else:
        print(count, end=' ')
