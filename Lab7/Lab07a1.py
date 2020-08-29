#Finished
user = []
d = 0

while d >= 0:

    d = int(input("Enter number of widgets (Negative number to cancel): "))
    if d < 0:
        break   #So 0 isn't added to user[]
    else:
        user.append(d)
for interval in range(1,len(user)):
    incr = 0            #Resets values back to 0 after calculations
    decr = 0
    same = 0
    for i in range(len(user)):
        if i+interval < len(user):
            if user[i] < user[interval+i]:
                incr += 1
            if user[i]> user[interval+i]:
                decr += 1
            if user[i] == user[interval+i]:
                same += 1

    per = incr/(incr+decr+same)*100
    otherone = format(per, '.1f')   #Formatting#
    dep = decr/(incr+decr+same)*100
    axel = format(dep, '.1f')       ##Formatting#
    sep = same/(incr+decr+same)*100
    print("For "+str(interval)+"-day intervals "+str(otherone)+"% were increasing and "+str(axel)+"% were decreasing.")


