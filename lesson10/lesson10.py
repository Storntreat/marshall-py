# Lesson 10
number = input()

telemarketer = True

if number[0] != '8' and number[0] != '9':
    telemarketer = False
if number[1] != number[2]:
    telemarketer = False
if number[3] != '8' and number[3] != '9':
    telemarketer = False
if telemarketer == False:
    print("Not Telemarketer")
if telemarketer == True:
    print("Telemarketer")
