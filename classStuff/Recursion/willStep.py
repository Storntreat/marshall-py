def stairs(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return stairs(n-2) + stairs(n-1)
def stairsDict(steps):
    answer = {0:0,1:1,2:2}
    
    if steps in answer:
        return answer[steps]
    else:
        for i in range (3,steps+1):
            answer[i] = answer[i-1] + answer[i-2]
        return answer[steps]
solutions = stairs(10)
print(solutions)