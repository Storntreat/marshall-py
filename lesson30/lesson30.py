# Lesson 30
N = int(input("Pick a length: "))
pattern = ""
for i in range(N):
    if i % 2 == 0:
        pattern += "1"
    else:
        pattern += "0"
    print(pattern)
