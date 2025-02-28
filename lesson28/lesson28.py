# Lesson 28
userInput = input()
i = 0
j = len(userInput)-1
condition = True
while i < len(userInput)-1:
    if userInput[i] != userInput[j]:
        print("False")
        condition = False
        i = len(userInput)
    i += 1
    j -= 1
if condition: 
        print("True")