# Lesson 7
import random
DC = int(input())
roll = random.randrange(1,20)
print(f"You rolled a {roll}.")
if DC >= roll:
    print(f"Success")
else:
    print(f"Failure")