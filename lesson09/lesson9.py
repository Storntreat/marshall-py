# Lesson 9
import random
validChoice = False
while validChoice == False:
    playerChoice = input("Enter a valid move: ")
    if playerChoice in {'rock', 'scissors', 'paper'}:
        validChoice = True

AiChoice = random.choice(['rock', 'scissors', 'paper'])

if playerChoice == AiChoice:
    print("Tie")
else:
    if playerChoice == 'rock':
        if AiChoice == 'scissors':
            print("Win")
        else:
            print("Lose")
    elif playerChoice == 'scissors':
        if AiChoice == 'rock':
            print("Lose")
        else:
            print("Win")
    else: 
        if AiChoice == 'rock':
            print("Win")
        else: 
            print("Lose")

