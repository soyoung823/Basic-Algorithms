# Recursive

def binary_search_recursive(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion.
    args:
        array: a sorted array of items of the same type
        target: the element you're searching for
    returns:
        int: the index of the target, if found, in the source
        -1: if the target is not found.
    '''
    mid = (start_index + end_index) // 2
    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return binary_search_recursive(array, target, mid + 1, end_index)
    else:
        return binary_search_recursive(array, target, start_index, mid - 1)

def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1], 0, len(array) - 1)
    if answer == test_case[2]:
        print('Pass!')
    else:
        print('Fail!')

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)