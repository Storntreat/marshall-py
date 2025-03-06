point = 0
word = input("Please input a string: ")
for i in range(len(word)):
        if word[i] in "bcdfghjklmnpqrstvwxyz":
            point += 5
        elif word[i] in "aeiou":
            point += 1
point = point*len(word)
lowPoint = point
lowest = word 
highPoint = point
highest = word

while True:
    point = 0
    if word == "X":
        break
    for i in range(len(word)):
        if word[i].isalpha and not word[i] in "aeiou" and not word[i] in "AEIOU":
            point += 5
        elif word[i].isalpha:
            point += 1
    point = point*len(word)
    if point <= lowPoint:
        lowPoint = point
        lowest = word
    elif point >= highPoint:
        highest = word
        highPoint = point
    word = input("Next string: ")

print(f"The lowest scoring word is {lowest} with a score of {lowPoint}.")
print(f"The highest scoring word is {highest} with a score of {highPoint}.")