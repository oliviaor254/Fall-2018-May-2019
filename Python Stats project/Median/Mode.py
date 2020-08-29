
##Look Over


def sorting(L):
    for val in range(len(L) - 1, 0, -1):  # selection sort
        maxpos = 0
        for sort_ in range(val + 1):
            if L[sort_] > L[maxpos]:  # Bubble sort in selection
                maxpos = sort_
        temp = L[val]
        L[val] = L[maxpos]
        L[maxpos] = temp
    return L


def Media(A):       # Works
    Med = 0
    A = sorting(A)
    print(A)
    if len(A)%2 == 0:
        Med = (A[int(len(A)/2)-1] + A[int((len(A)/2))])/2
    else:
        Med = A[int(len(A)/2)]
    return Med



#def MoDe(L):        # NEEDS WORK
#    Mode = 0
#    spot = 0
#    for n in range(len(L)):
#        ct = L.count(L[n])
#        if ct > Mode:
#            Mode = ct
#            spot = n
#    return L[spot]


Listo = [1, 15, 15, 15, 3, 3, 15,5]
print(Listo)
print(Media(Listo))