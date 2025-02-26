counter = 0
number = input("Enter a number: ")
length = len(number)

while length > 1:
    i = 0
    digit = 0
    while i < length:
        digit += int(number[i])
        i += 1
    number = digit
    number = str(number)
    length = len(number)
    counter += 1

print(f"You need to add its digits {counter} times to get to a sum of a single digit.")