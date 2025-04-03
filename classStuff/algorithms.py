#linear search
def linear(array,target):
    #array.find(target) or array.index(target)
    if not array:
        return -1
    elif len(array) == 1:
        if array[0] == target:
            return 0
        else:
            return -1
    else: #array has 2 or more values
        for i in range(0, len(array)):
            if array[i] == target:
                return i
        # no need to check bc if loop finishes we know its not in there
        return -1

#binary search
def binary(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] > target:
            right = middle - 1
        else: 
            left = middle + 1
    return -1 #if no value is found


#bubble sort
def bubble(array):
    if len(array) <= 1:
        return array
    swap = True
    while swap:
        swap = False
        for i in range(1, len(array)):
            if array[i] < array[i-1]:
                array[i], array[i-1] == array[i-1], array[i]
    return array

#insertion sort
def insertion(array):
    if len(array) <= 1:
        return array
    else:
        for i in range(1, len(array)):
            for j in range(i, 0, -1):
                if array[j-1] > array[j]:
                    array[j-1], array[j] == array[j], array[j-i]
                else: 
                    break
    return array


#selection sorts
def select1(array):
    result = []
    while array:
        result.append(min(array))
        array.remove(min(array))
    return result

def select2(array):
    result = []
    while array:
        smallest = min(array)
        result.append(smallest)
        array.remove(smallest)
    return result

def select3(array):
    def smallFinder(array, start=0):
        if not array:
            return None
        elif len(array) == 1:
            return array[0]
        else:
            location = start
            smallest = array[start]
            for i in range(start+1, len(array)):
                if array[i] < smallest:
                    smallest = array[i]
                    location = i
            return location
    if len(array) <= 1:
        return array
    else: 
        for i in range(i, len(array)):
            next_smallest = smallFinder(array, start=i)
            array[i-1], array[next_smallest] = array[next_smallest],array[i-1]
    return array

#predetermined argument
def f(x,y,z=0):
    return x + y + z
#inputted arguments take prioirty of predetermined
#predetermined go at the end
