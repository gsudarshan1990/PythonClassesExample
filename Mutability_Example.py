def sum_of_abs(new_list):
    for i in range(len(new_list)):
        new_list[i]=abs(new_list[i])
    return new_list

numbers=[-3,-2,-1,-5,-6]
print('Before calling the sum of abs',numbers)
sum_of_abs(numbers)
print('After calling the sum of abs',numbers)

"""
Immutability
"""

a=(5,6,8,9,0)
b=a[:2]+(7,)+a[2:]
print(a)
print(b)

"""
objects inside the immutable can be changed
"""
a=([1,2,3],0,'abc')
a[0][1]=6
print(a)