"""
This is our main testing program to test if merge sort is working correctly
"""

from hw2_debugging import merge_sort

def test_empty_array():
    """Tests the mergeSort function on an empty array"""
    arr = []
    assert merge_sort(arr) == arr

def test_array_1():
    """Tests the mergeSort function on an array with 1 value (odd number of values)"""
    arr = [1]
    assert merge_sort(arr) == arr

def test_array_even():
    """Tests the mergeSort function on an array with 4 values (even number of values)"""
    arr = [3, 1, 2, 4] 
    arr2 = [1,2,3,4]
    assert merge_sort(arr) == arr2
