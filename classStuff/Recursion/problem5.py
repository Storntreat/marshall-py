a_list = [1,3,5,2,4,9,1,13,34,567,41,34,234,44,23,123]
def max(n):
    if len(n) == 0:
        return None
    elif len(n) == 1:
        return n[0]
    elif len(n) == 2:
        if n[0] > n[1]:
            return n[0]
        else:
            return n[1]
    else:
        if n[0] > n[1]:
            n[0],n[1] = n[1],n[0]
            return max(n[1:])
        else:
            return max(n[1:])
maxA = max(a_list)
print(maxA)