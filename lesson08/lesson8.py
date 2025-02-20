# Lesson 8

wins = 0
counter = 0
while counter < 6:
    game = input()
    if 'W' in game:
        wins += 1
    counter += 1
if game == range(1,3)