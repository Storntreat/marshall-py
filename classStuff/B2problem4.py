number = int(input())
scores = []
counter = 0
numBronze = 1
bronze = 0
for i in range(0,number):
    scores.append(int(input()))
scores.sort()
for i in range(number-2,-1,-1):
    if scores[i] < scores[i+1]:
        counter += 1
    if counter == 2:
        bronze = scores[i]
        if scores[i] == scores[i+1]:
            numBronze += 1
print(f"{bronze} {numBronze}")