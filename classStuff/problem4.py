a = input()
i = 0

#4a) 
while i < len(a):
    if a[i] == "@":
        print(i)
        i += 1
        break;
    i += 1

#4b)
while i < len(a):
    if a[i] == "@":
        print(i)
    i += 1
print(" ")

#4c) (if it was lowest to highest ascii numbers sorted it would work)
i = 0
while i < len(a):
    print(ord(a[i]))
    if ord(a[i]) == 64:
        print(i)
    elif ord(a[i]) > 64:
        break
    i +=1

