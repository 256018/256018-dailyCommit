def replace(l):
    for i in range(0,len(l),2):
        l[i],l[i+1]=l[i+1],l[i]
    return l
l=[1,2,5,3,7,8,9,10]
print(replace(l))
