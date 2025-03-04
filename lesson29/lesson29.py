# Lesson 29
a = input("Input string: ")
counter = 0
for i in range(len(a)):
    if a[i].isalpha():
        if a[i] not in "aeiou":
            counter += 1
print(f"Number of consonants is: {counter}.")