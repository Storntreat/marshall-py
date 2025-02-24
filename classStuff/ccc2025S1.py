user_input = [int(x) for x in input().split()]
A, B, X, Y = user_input

sides = 2*A + 2*X + 2*max(B,Y)
stack = 2*B + 2*Y + 2*max(A,X)
perimeter = min(stack,sides)
print(perimeter)