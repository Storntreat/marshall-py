# Lesson 33
a_list = [1,2,3,6,1,2,4,6,1,3,5,7,8,2,3,5,7,2,3,5,2,5,5,5,5,3,5,4,6,2,1,1,2,5,6,7,7,6,-11]
def mean(list):
    sum = 0
    for i in list:
        sum += i
    sum = sum / len(list)
    return sum

def median(list):
    list.sort()
    if len(list) % 2 == 0:
        middle = (list[int(len(list)/2)] + list[int((len(list)/2)-1)])/2
    else:
        middle = list[int(len(list)/2)]
    return middle
print(mean(a_list))
print(median(a_list))
