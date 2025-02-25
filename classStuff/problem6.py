N = input()
N = int(N)
counter = 0
while N != 1:
    if N % 2 == 0:
        N = N/2
    else:
        N = 3*N + 1
    N = int(N)
    print(N)
    counter += 1
print(f"number of steps: {counter}")