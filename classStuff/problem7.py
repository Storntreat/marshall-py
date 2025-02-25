string1 = input()
string2 = input()
i = 0
j = 0
newString = ""
while i < len(string1) and j < len(string2):
    ascii1 = ord(string1[i])
    ascii2 = ord(string2[j])
    if ascii1 <= ascii2:
        newString += chr(ascii1)
        i += 1
    else:
        newString += chr(ascii2)
        j += 1
while i < len(string1):
    newString += string1[i]
    i += 1
while j < len(string2):
    newString += string2[j]
    j += 1
print(newString)