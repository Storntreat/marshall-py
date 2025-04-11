import numpy as np

# define input signal
N = int(input("Number of Intervals: "))
a_list = []
for i in range(N):
    a_list.append(float(input(f"Value at n={i}: ")))
signal = np.array(a_list)

# DFT implementation
def DFT(x):
    N = len(x)
    X = []

    for k in range(N):
        X_k = 0

        for n in range(N):
            e = np.exp(2j * np.pi * k * n / N)
            X_k += x[n] / e

        X.append(X_k)

    return np.array(X)

X_dft = DFT(signal)

print(f"Signal: {signal}")
print(f"DFT Result: {X_dft}")