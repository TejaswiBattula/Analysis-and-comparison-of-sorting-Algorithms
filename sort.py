import sys
# when dealing with bucket short the array size greater than 2000 seems to take a lot of time on my system and freeze
# the computer
sys.setrecursionlimit(10 ** 6)
MIN_MERGE = 32

#
#        Quick Sort
#
# Function to find the partition position
# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def QuickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    QuickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    QuickSort(array, pi + 1, high)

def quickSort(arr):
    n = len(arr)
    QuickSort(arr, 0, n-1)

# def quickSort(arr):
#     n = len(arr)
#     QuickSort(arr, 0, n-1)

#
#    Heap Sort
#
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 
 # See if left child of root exists and is
 # greater than root
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
 # See if right child of root exists and is
 # greater than root
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
 # Change root, if needed
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
 
  # Heapify the root.
 
        heapify(arr, n, largest)
 
 
# The main function to sort an array of given size
 
def heapSort(arr):
    n = len(arr)
 
 # Build a maxheap.
 # Since last parent will be at (n//2) we can start at that location.
 
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
 
 # One by one extract elements
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)


#
#   Merge Sort
#
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def MergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        MergeSort(arr, l, m)
        MergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def mergeSort(arr):
    n = len(arr)
    MergeSort(arr, 0, n-1)


#
#    Radix Sort
#
# A function to do counting sort of arr[] according to 
# the digit represented by exp. 
def countingSort(arr, exp1): 
   
    n = len(arr) 
   
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
   
    # initialize count array as 0 
    count = [0] * (10) 
   
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[int((index)%10)] += 1
   
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
   
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        i -= 1
   
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
 
# Method to do Radix Sort
def radixSort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 // exp > 0:
        countingSort(arr,exp)
        exp *= 10


#
#    Bucket Sort
#
def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

def bucketSort(input_list):
    # Check if the input_list is empty
    if not input_list:
        return input_list

    # Find the minimum and maximum values in the list
    min_value, max_value = min(input_list), max(input_list)
    
    # Calculate the range of values and set the size of each bucket
    value_range = max_value - min_value
    size = value_range / len(input_list) if len(input_list) != 0 else 1

    # Create n empty buckets where n is equal to the length of the input list
    buckets_list = [[] for _ in range(len(input_list))]

    # Put list elements into different buckets based on their value range
    for i in range(len(input_list)):
        # Handle the case where size is zero
        if size != 0:
            # Use integer division (//) to ensure j is an integer
            j = int((input_list[i] - min_value) / size)
        else:
            j = 0

        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    # Sort elements within the buckets using Insertion Sort
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
            
    # Concatenate buckets with sorted elements into a single list
    final_output = []
    for x in range(len(input_list)):
        final_output.extend(buckets_list[x])
    
    return final_output

#
#   Tim Sort
#
# Python3 program to perform basic timSort 
MIN_MERGE = 32
  
  
def calcMinRun(n): 
    """Returns the minimum length of a 
    run from 23 - 64 so that 
    the len(array)/minrun is less than or 
    equal to a power of 2. 
  
    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33, 
    ..., 127=>64, 128=>32, ... 
    """
    r = 0
    while n >= MIN_MERGE: 
        r |= n & 1
        n >>= 1
    return n + r 
  
  
# This function sorts array from left index to 
# to right index which is of size atmost RUN 
def insertionSort(arr, left, right): 
    for i in range(left + 1, right + 1): 
        j = i 
        while j > left and arr[j] < arr[j - 1]: 
            arr[j], arr[j - 1] = arr[j - 1], arr[j] 
            j -= 1
  
  
# Merge function merges the sorted runs 
def merge(arr, l, m, r): 
  
    # original array is broken in two parts 
    # left and right array 
    len1, len2 = m - l + 1, r - m 
    left, right = [], [] 
    for i in range(0, len1): 
        left.append(arr[l + i]) 
    for i in range(0, len2): 
        right.append(arr[m + 1 + i]) 
  
    i, j, k = 0, 0, l 
  
    # after comparing, we merge those two array 
    # in larger sub array 
    while i < len1 and j < len2: 
        if left[i] <= right[j]: 
            arr[k] = left[i] 
            i += 1
  
        else: 
            arr[k] = right[j] 
            j += 1
  
        k += 1
  
    # Copy remaining elements of left, if any 
    while i < len1: 
        arr[k] = left[i] 
        k += 1
        i += 1
  
    # Copy remaining element of right, if any 
    while j < len2: 
        arr[k] = right[j] 
        k += 1
        j += 1
  
  
# Iterative Timsort function to sort the 
# array[0...n-1] (similar to merge sort) 
def timSort(arr): 
    n = len(arr) 
    minRun = calcMinRun(n) 
  
    # Sort individual subarrays of size RUN 
    for start in range(0, n, minRun): 
        end = min(start + minRun - 1, n - 1) 
        insertionSort(arr, start, end) 
  
    # Start merging from size RUN (or 32). It will merge 
    # to form size 64, then 128, 256 and so on .... 
    size = minRun 
    while size < n: 
  
        # Pick starting point of left sub array. We 
        # are going to merge arr[left..left+size-1] 
        # and arr[left+size, left+2*size-1] 
        # After every merge, we increase left by 2*size 
        for left in range(0, n, 2 * size): 
  
            # Find ending point of left sub array 
            # mid+1 is starting point of right sub array 
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
  
            # Merge sub array arr[left.....mid] & 
            # arr[mid+1....right] 
            if mid < right: 
                merge(arr, left, mid, right) 
  
        size = 2 * size 