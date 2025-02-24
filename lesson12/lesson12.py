# Lesson 12
angle1 = input()
angle1 = int(angle1)
angle2 = input()
angle2 = int(angle2)
angle3 = input()
angle3 = int(angle3)
sum = angle1+angle2+angle3

if sum != 180:
    print("Error")
else:
    if angle1 == angle2 == angle3:
        print("Equilateral")
    else:
        if angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
            print("Isosceles")
        else:
            print("Scalene")