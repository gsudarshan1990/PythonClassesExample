"""
We are given an array A consisting of N distinct integers.We would like to sort array A into ascending order using a simple algorithm. First, we divide it into one
or more slices. Then we sort each slice.After that we join the sorted slices in the same order. Write a function solution that returns the maximum number of slices
for which the algorithm will return a correctly sorted array.

Given A=[2,4,1,6,5,9,7] the funciton returns 3. The array can be split into three slices:[2,4,1],[6,5] and[9,7]. Then after sorting each slice and joining them together,
while array will be sorted into ascending order.

Given A=[4,3,2,6,1] the function returns 1 as the function cannot split into smaller sizes as it has to be sorted all at once.

Given A=[2,1,6,4,3,7] the function should return 3

"""


import copy
def solutions(A):
    new_array=copy.deepcopy(A)
    A.sort()
    final =0
    unsorted_sum = 0
    sorted_sum = 0
    for i in range(len(A)):
        unsorted_sum+=new_array[i]
        sorted_sum+=A[i]
        if sorted_sum == unsorted_sum:
            final+=1
        else:
             0
    print(final)

A=[2,4,1,6,5,9,7]
solutions(A)