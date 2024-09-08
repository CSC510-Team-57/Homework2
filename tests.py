from hw2_debugging import *

# Tests the mergeSort function on an empty array
def test_empty_array(): 
  arr = []
  assert merge_sort(arr) == arr

# Tests the mergeSort function on an array with 1 value (odd number of values)
def test_array_1():
  arr = [1]
  assert merge_sort(arr) == arr

# Tests the mergeSort function on an array with 4 values (even number of values)
def test_array_even():
  arr = [3, 1, 2, 4] 
  arr2 = [1,2,3,4]
  assert merge_sort(arr) == arr2
  
  
  
    
