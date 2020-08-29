golf = {}
score1 = 0
score2 = 0
name = ''
scores= []
med = 0
while score1>=0:
    score1 = int(input("Enter score for round 1: "))
    if score1< 0:
        break
    score2 = int(input("Enter score for round 2: "))
    name = input("Enter name ")
    scores.append(score1+score2)
    golf.update({name: score1+score2})
print(golf)
print("scores",scores)
for scorepos in range(len(scores)-1,0,-1):      #selection sort
    maxpos = 0
    for sort_ in range(scorepos+1):
        if scores[sort_] > scores[maxpos]:      #Bubble sort in selection
            maxpos = sort_
    temp = scores[scorepos]
    scores[scorepos] = scores[maxpos]
    scores[maxpos] = temp
print(scores)
median = 0
if len(scores)%2 == 0:
    med = len(scores)/2                               #OR IF SCORE IS EQUAL TO THE PERSON'S WE JUST PRINT THAT INSTEAD OF UPDATING THE DICTIONARY
    median = (scores[int(med)]+scores[int(med-1)])/2
else:
    med = len(scores)/2
    median = scores[int(med)]
print(median)
for a,v in golf.items():
    if golf.get(a, v) >= median:
        print(a, " moves on to the 3rd round")
    if golf.get(a, v) < median:
        print(a, " does not move on to the next round")



