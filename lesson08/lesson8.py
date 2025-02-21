# Lesson 8

wins = 0
counter = 0
while counter < 6:
    game = input()
    if 'W' in game:
        wins += 1
    counter += 1
if wins == 1 or wins == 2:
    print("Group 3")
elif wins == 3 or wins == 4:
    print("Group 2")   
elif wins == 5 or wins == 6:
    print("Group 1")   
else:
    print("Disqualified")