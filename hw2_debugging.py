"""
This file contains the mergesort function which sorts an array by splitting the array and then
sorting the halves while merging
"""

import rand

def merge_sort(arr):
    """
    Main Merge Sort function which takes in an array to be sorted, and then splits it to be sorted,
    by recusively calling itself until the amount of indexes in the array is only one. It then
    merges them, while sorting until it sorts the entire array which it then outputs.
    """
    if len(arr) == 1:
        return arr

    half = len(arr) // 2
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, right_arr):
    """
    Helper function for Merge Sort which takes in two arrays and recombines them, but it does sort
    them while recombining.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    merge_arr[left_index + right_index:] = left_arr[left_index:] + right_arr[right_index:]
    return merge_arr

# Creates a random array and then sorts it with mergesort
tempArr = rand.random_array([None] * 20)
arr_out = merge_sort(tempArr)

# Prints the sorted array
print(arr_out)