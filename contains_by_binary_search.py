'''
Contains
The second variation is a function that returns a boolean value indicating whether an element is present, but with no information about the location of that element.
For example:
letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) ## True
print(contains('b', letters)) ## False
There are a few different ways to approach this, so try it out, and we'll share two solutions after.
'''
def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source) - 1) // 2
    if source[center] == target:
        return center
    elif target < source[center]:
        return recursive_binary_search(target, source[:center], left)
    else:
        return recursive_binary_search(target, source[center + 1:], left + center + 1)

# recursive
def contains_recursive(target, source):
    return recursive_binary_search(target, source) is not None

# iterative
def contains(target, source):
    min = 0
    max = len(source) - 1
    while min <= max:
        mid = (min + max) // 2
        if target == source[mid]:
            return True
        elif target < source[mid]:
            max = mid - 1
        else:
            min = mid + 1
    return False

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) ## True
print(contains('b', letters)) ## False

answers = [contains('a', letters), contains('b', letters), contains_recursive('a', letters), contains_recursive('b', letters)]
for answer in answers:
    if answer == True:
        print('Pass!')
    else:
        print('Fail!')