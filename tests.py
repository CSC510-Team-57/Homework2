import pytest
import hw2_debugging

def test_empty_array(): 
  arr = []
  assert mergeSort(arr) == arr

def test_array_1():
  arr = [1]
  assert mergeSort(arr) == arr

def test_array_even():
  arr = [3, 1, 2, 4]
  arr2 = [1,2,3,4]
  assert mergeSort(arr) == arr2
  
  
  
    
