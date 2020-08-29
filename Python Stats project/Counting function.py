print(2+43)
YN = input("Save data of column 2 as .jpeg (Y or N)? ")  # HANDLE IF NOT THE WRITE INPUT
while YN.isdigit() or (YN != 'N' and YN != 'Y'):
    YN = input("That is not the correct format. Please enter Y or N \n Save data of column 2 as .jpeg (Y or N)? ")
    if YN == 'Y':
        print("You saved it!")
        continue
    if YN == 'N':
        print("ITs staying!")
        continue
print(2*'Howdy')

''''''