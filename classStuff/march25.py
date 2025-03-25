#define functions
def selectionsort(array):
    sorted_list = []
    while len(array) > 0:
        smallest = min(array)
        sorted_list.append(smallest)
        array.remove(smallest)
    return sorted_list

def createlist(size):
    result = []
    for i in range(size):
        result.append(int(input("Enter a number: ")))
    return result
#use functions and inputs

a_list = createlist(int(input("Enter length of list: ")))
print(selectionsort(a_list))
print(a_list)