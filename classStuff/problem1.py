number = int(input())
counter = 1
divisorSum = 0
while counter < number:
    if number % counter == 0:
        divisorSum += counter
    counter += 1

if divisorSum < number:
    print(f"The number {number} is deficient.")
elif divisorSum > number:
    print(f"The number {number} is abundant.")
else:
    print(f"The number {number} is perfect.")