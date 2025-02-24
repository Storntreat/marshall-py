words = input()
index = 0
temp = ""
while index < len(words):
    temp += words[index]
    if words[index] == " ":
        print(temp)
        temp = ""
    index += 1
print(temp)