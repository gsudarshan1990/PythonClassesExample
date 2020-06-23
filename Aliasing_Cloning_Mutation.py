"""
With your knowledge of the concepts of aliasing, mutation, and cloning, fix this program so that the original list is not mutated. (Please, only modify the body of the functions).
"""
import copy
a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c


def remove_elem(data, target):
    new_list=data[:]
    for item in data:
        if item == target:
            new_list.remove(target)
    return new_list


def get_product(data):
    new_list=data[:]
    total = 1
    for i in range(len(data)):
        total *= new_list.pop()
    return total


remove_elem(c, 3)
print(get_product(b))
print(a)