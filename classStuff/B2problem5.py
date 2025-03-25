a_list = [67545676,98765,98989,9,89,89,98,98,98,9,98,9,89,89,89,8,9,1234,1234123,42134,1243,21344,444324,4434] #or list
b_list = []
while a_list:
    minimum = float('inf')
    for i in range(len(a_list)):
        minimum = min(minimum,a_list[i])
    b_list.append(minimum)
    a_list.remove(minimum)
print(b_list)