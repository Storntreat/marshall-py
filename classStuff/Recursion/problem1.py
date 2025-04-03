#factorial
def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)

#testing max
i = 0
while True:
    i += 1
    print(i)
    print(fact(i))

#ok most is 999