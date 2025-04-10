firstInput = input()
inputArr = list(firstInput.split())
cards = []
length = int(inputArr[0])
for i in range(length):
    cards.append(0)
turns = int(inputArr[1])
for i in range(turns):
    yrng = input()
    yrngArr = list(yrng.split())
    left = int(yrngArr[0])
    right = int(yrngArr[1])
    for j in range(left-1, right):
        if cards[j] == 0:
            cards[j] = 1
        else:
            cards[j] = 0
counter = 0
for i in range(len(cards)):
    if cards[i] == 0:
        counter += 1
print(counter)
