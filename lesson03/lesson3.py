# Lesson 3
area = input()
area = int(area)

# sideLength = 1     # original solution
# while sideLength**2 <= area:
#     sideLength += 1
# else:
#     sideLength -= 1
#     print("The largest square has side length is", sideLength, ".")

sideLength = area ** 0.5
sideLength = int(sideLength // 1)

print(f"The largest square has side length {sideLength}.")