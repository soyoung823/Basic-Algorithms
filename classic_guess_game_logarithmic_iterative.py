'''
Binary search practice
Let's get some practice doing binary search on an array of integers. 
We'll solve the problem two different ways—both iteratively and resursively.
Here is a reminder of how the algorithm works:
Find the center of the list (try setting an upper and lower bound to find the center)
Check to see if the element at the center is your target.
If it is, return the index.
If not, is the target greater or less than that element?
If greater, move the lower bound to just above the current center
If less, move the upper bound to just below the current center
Repeat steps 1-6 until you find the target or until the bounds are the same or cross (the upper bound is less than the lower bound).
Problem statement:
Given a sorted array of integers, and a target value, find the index of the target value in the array. 
If the target value is not present in the array, return -1.
'''
# Iterative solution
# First, see if you can code an iterative solution (i.e., one that uses loops). If you get stuck, the solution is below.

def binary_search(array, target):
    
    min = 0
    max = len(array) - 1
    
    while min <= max:
        mid = (min + max) // 2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            min = mid + 1
        else:
            max = mid - 1
    return -1


for r in [4, 3, 7, 6, 100]:
    array = [r for r in range(r)]
    print(array)
    for i in range(r):
        result = binary_search(array, i)
        assert result == i, 'r={} i={} result={}'.format(r, i, result)


def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print('Pass!')
    else:
        print('Fail!')

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)

'''
TC: log n since:
n * (1 / 2)^S = 1
negative exponents to rearrange the fraction
n * 2^(-S) = 1
n = 1 / 2^(-S)
n = 2^S
log2 (n) = S
S (time complexity) = log n

SC: O(n)
'''