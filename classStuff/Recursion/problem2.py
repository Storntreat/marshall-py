# Exponentiation

#Write a program that evaluates the power to its integer representation.

# a^b

def exp(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * exp(a,b-1)
