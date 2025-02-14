# Lesson 4

import math

frequency = len(input())
frequency += len(input())
frequency += len(input())
print(frequency)

dozens = math.ceil(frequency / 12)
print(dozens*12 - frequency)
print(dozens*14.95)

#git add lessonN.py
#git commit -m "solved lesson N"
#git push
