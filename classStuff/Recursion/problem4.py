def rev(n):
    if len(n) == 0:
        return n
    elif len(n) == 1:
        return n
    elif len(n) == 2:
        m = list(n)
        m[0], m[-1] = m[-1], m[0]
        return "".join(m)
    else:
        return n[-1] + rev(n[0:-1])
print(rev("12345678"))