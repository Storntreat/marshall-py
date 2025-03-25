aList = [2,1,6,1,5,3,4,7] 
sorted = True
while sorted:
    sorted = False
    for i in range(1,len(aList)):
        right = aList[i]
        for j in range(i-1,-1,-1):
            left = aList[j]
            if not left > right:
                sorted = True
                aList[j], aList[i] = aList[i], aList[j]
 
bList = [2,1,6,1,5,3,4,7] 
for i in range(1,len(bList)):
    for j in range(i,0,-1):
        if bList[j] < bList[j-1]:
            bList[j-1],bList[j] = bList[j],bList[j-1]
        else:
            break