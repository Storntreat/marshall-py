a_list = []
size = int(input())
for i in range(size):
    a_list.append(input())
target = int(input())

#for i in range(size):
#    if a_list[i] == target:
#        print(f"Index of target value is: {a_list[i]}.")
#        break

a_list.sort()
left = 0
right = size-1
inText = False
while left < right:
    middle = (left + right)//2
    if middle == target:
        print(f"Index found at {middle}")
        inText = True
    elif middle < target:
        left = middle + 1
    else:
        right = middle - 1
if inText:
    print("Not Found")