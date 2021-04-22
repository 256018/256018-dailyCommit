l=[3,4,1,2,8,9]
firstmin=l[0]
secondmin=l[0]
for i in l:
    if (i<firstmin):
        secondmin = firstmin
        firstmin = i
for i in l:
    if (i < secondmin and i != firstmin):
        secondmin = i
print(secondmin)
