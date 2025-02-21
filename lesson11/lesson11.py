# Lesson 11
coord = input()
coord = coord.split(' ')
coord = list(map(int, coord))
x,y = coord

if x < 0:
    if y < 0:
        print(3)
    else:
        print(2)
else:
    if y < 0:
        print(4)
    else:
        print(1)