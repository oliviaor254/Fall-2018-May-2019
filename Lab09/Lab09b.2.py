# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Olivia Ornelas
# Section: 514
# Assignment: Lab 09b-2
# Date: 30 October 2018
loan_amnt1 = int(input("What is the loan ammount? "))
aintrate = float(input("What is the annual interest rate (as a decimal)? "))
monthly_pay = float(input("How much is the monthly payments? "))
file = input("What file do you want to save the results to? ")
file = file+'.csv'  #Formats file to CSV
tot_remain = 0
count = 0
loan_amntleft = loan_amnt1
out_file = open(file, 'w')
out_file.write("Month, Interest, Amount remaining \n")
while count <= 30 and loan_amnt1 >= 0:
    if loan_amnt1 < 0 or count < 30:
        break
    out_file.write(str(count)+','+str(tot_remain)+','+str(loan_amnt1)+'\n') #Adds to coad each time while in loop
    tot_remain += aintrate*(1/12)
    loan_amntleft = (loan_amnt1 - monthly_pay)+tot_remain
    loan_amnt1 = loan_amntleft
    count += 1
out_file.close()
