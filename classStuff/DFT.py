import numpy as np
import matplotlib.pyplot as plt

# Define a simple signal (e.g., 4 points)
N = int(input("Number of Time Indexes: "))
a_list = []
for i in range(N):
    a_list.append(float(input(f"Value at n={i}: ")))
signal = np.array(a_list)

# DFT Implementation
def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

# Perform DFT
X_dft = dft(signal)

print("Signal:", signal)
print("DFT Result:", X_dft)

# Visualizing the Magnitudes
plt.figure(figsize=(10, 5))
plt.stem(np.arange(N), np.abs(X_dft), linefmt='b-', markerfmt='bo', basefmt=' ')  # DFT Magnitudes
plt.title('Magnitude Spectrum using DFT')
plt.xlabel('Frequency Index (k)')
plt.ylabel('Magnitude')
plt.grid()
plt.show()