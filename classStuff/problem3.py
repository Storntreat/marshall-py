number = input()
number = int(number)
divisor = 3
while number % 2 == 0:
    print(2)
    number = number / 2
while number >= 1:
    if number % divisor == 0:
        print(divisor)
        number = number / divisor
        
