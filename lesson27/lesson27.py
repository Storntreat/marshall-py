# Lesson 27

def alphacleaner(text):
    new = ""
    for c in text:
        if c.isalpha():
            new += c
    return new

string = input()
print(alphacleaner(string))