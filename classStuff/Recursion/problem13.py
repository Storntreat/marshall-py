def factorize(n):
    factor_list = []
    for i in range(n, 0, -1):
        if n % i == 0:
            factor_list.append(i)
    return factor_list

def gcd(a,b):
    factors_a = factorize(a)
    factors_b = factorize(b)
    for value in factors_a:
        if value in factors_b:
            return value
    return 1

a = int(input("A = "))
b = int(input("B = "))
gcF = gcd(a,b)
print(gcF)

def recursiveGCD(a,b):
    if b == 0:
        return a
    else:
        return recursiveGCD(b, a % b)

