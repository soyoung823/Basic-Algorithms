'''
Problem statement
Given a sorted array that may have duplicate values, use binary search to find the first and last indexes of a given value.
For example, if you have the array [0, 1, 2, 2, 3, 3, 3, 4, 5, 6] and the given value is 3, 
the answer will be [4, 6] (because the value 3 occurs first at index 4 and last at index 6 in the array).
The expected complexity of the problem is  𝑂(𝑙𝑜𝑔(𝑛))

'''
def first_and_last_index_error(arr, number):
    '''
    Given a sorted array that may have duplicate values, 
    use binary search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    '''
    min_i = 0
    max_i = len(arr) - 1

    possible_i = 0

    while min_i <= max_i:
        mid_i = (min_i + max_i) // 2
        if number == arr[mid_i]:
            possible_i = mid_i
        elif number < arr[mid_i]:
            max_i = mid_i - 1
        else:
            min_i = mid_i + 1

    min_i_n = possible_i
    max_i_n = possible_i

    while arr[min_i_n] == number:
        min_i_n -= 1

    while arr[max_i_n] == number:
        max_i_n += 1

    return [min_i_n, max_i_n]

def find_start_index(arr, number, start_index, end_index):
    # binary search solution to search for the first index of the array
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index) // 2

    if arr[mid_index] == number:
        current_start_pos = find_start_index(arr, number, start_index, mid_index - 1)
        if current_start_pos != -1:
            start_pos = current_start_pos
        else:
            start_pos = mid_index
        return start_pos
    elif arr[mid_index] < number:
        return find_start_index(arr, number, mid_index + 1, end_index)
    else:
        return find_start_index(arr, number, start_index, mid_index - 1)

def find_end_index(arr, number, start_index, end_index):
    # binary search solution to search for the last index of the array
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index) // 2

    if arr[mid_index] == number:
        current_end_pos = find_end_index(arr, number, mid_index + 1, end_index)
        if current_end_pos != -1:
            end_pos = current_end_pos
        else:
            end_pos = mid_index
        return end_pos
    elif arr[mid_index] < number:
        return find_end_index(arr, number, mid_index + 1, end_index)
    else:
        return find_end_index(arr, number, start_index, mid_index - 1)


def first_and_last_index(arr, number):
    # search first occurence
    first_index = find_start_index(arr, number, 0, len(arr) - 1)

    # search last occurence
    last_index = find_end_index(arr, number, 0, len(arr) - 1)
    return [first_index, last_index]
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    answer = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == answer:
        print('Pass!')
    else:
        print('Fail!')

input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)