string = input("String: ")
shift = input("Shift: ")
shift = int(shift)
valid = False
while valid == False:
    if shift in range(-26,27):
        valid = True
    elif shift > 26:
        shift -= 26
    else:
        shift += 26

i = 0
newChar = 0
temp = ""
while i < len(string):
    if ord(string[i]) in range(65, 91):
        newChar = ord(string[i]) + shift
        if newChar > 90:
            newChar -= 26
        elif newChar < 65:
            newChar += 26
        temp += chr(newChar)
    else:
        temp += string[i]
    i += 1
print(temp)