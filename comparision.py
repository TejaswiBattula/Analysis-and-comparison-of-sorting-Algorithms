import sort
import time
import random
import plot
import math
import numpy as np


def RandomFrom0ToN(n):
    array = []
    for i in range(0, n):
        array.append(random.randint(0, n))
    return array

def RandomFrom0ToK(n):
    array = []
    k = 999
    for i in range(0, n):
        array.append(random.randint(0, k))
    return array

def RandomFrom0ToNCube(n):
    array = []
    cube = n*n*n
    for i in range(0, n):
        array.append(random.randint(0, cube))
    return array

def RandomFrom0ToLogN(n):
    array = []
    logn = int(math.log(n))
    for i in range(0, n):
        array.append(random.randint(0, logn))
    return array

def RandomMultiplesOf1000(n):
    array = []
    
    for _ in range(n):
        # Generate a random multiple of 1000
        multiple_of_1000 = random.randint(0, n // 1000) * 1000
        array.append(multiple_of_1000)
    
    return array

def RandomValuesSwaping(n):
    sequence = list(range(n + 1))

    # Perform swaps to create a partially shuffled sequence
    for _ in range(n // 2):
        index1, index2 = random.sample(range(n + 1), 2)
        sequence[index1], sequence[index2] = sequence[index2], sequence[index1]

    return sequence


def generateGraph():
    print("started")
    scenarios = [RandomFrom0ToN, RandomFrom0ToK, RandomFrom0ToNCube, RandomFrom0ToLogN, RandomMultiplesOf1000, RandomValuesSwaping]
    #sorting_algorithms = [quickSort, heapSort, mergeSort, radixSort, bucketSort, timSort]
    quickSort_duration_list = []
    heapSort_duration_list = []
    mergeSort_duration_list = []
    radixSort_duration_list = []
    bucketSort_duration_list = []
    timSort_duration_list = []

    length_lists = []
    
    for scenario in scenarios:
        length_list = []
        points = 50
        n = 100
        quickSort_duration = []
        heapSort_duration = []
        mergeSort_duration = []
        radixSort_duration = []
        bucketSort_duration = []
        timSort_duration = []

        while points:
            array = scenario(n)
            quickSort_array = array.copy()
            heapSort_array = array.copy()
            mergeSort_array = array.copy()
            radixSort_array = array.copy()
            bucketSort_array = array.copy()
            timSort_array = array.copy()

            # quick sort
            quickSort_start_time = time.time()
            sort.quickSort(quickSort_array)
            quickSort_end_time = time.time()
            quickSort_duration.append(quickSort_end_time - quickSort_start_time)

            # heapSort
            heapSort_start_time = time.time()
            sort.heapSort(heapSort_array)
            heapSort_end_time = time.time()
            heapSort_duration.append(heapSort_end_time - heapSort_start_time)

            # mergeSort
            mergeSort_start_time = time.time()
            sort.mergeSort(mergeSort_array)
            mergeSort_end_time = time.time()
            mergeSort_duration.append(mergeSort_end_time - mergeSort_start_time)

            # radixSort      
            radixSort_start_time = time.time()
            sort.radixSort(radixSort_array)
            radixSort_end_time = time.time()
            radixSort_duration.append(radixSort_end_time - radixSort_start_time)

            # bucketSort
            bucketSort_start_time = time.time()
            sort.bucketSort(bucketSort_array)
            bucketSort_end_time = time.time()
            bucketSort_duration.append(bucketSort_end_time - bucketSort_start_time)

            # timSort
            timSort_start_time = time.time()
            sort.timSort(timSort_array)
            timSort_end_time = time.time()
            timSort_duration.append(timSort_end_time - timSort_start_time)

            length_list.append(n)
            print(n)
            # print(end_time - start_time)
            points -= 1
            n += 1000

        quickSort_duration_list.append(quickSort_duration)
        heapSort_duration_list.append(heapSort_duration)
        mergeSort_duration_list.append(mergeSort_duration)
        radixSort_duration_list.append(radixSort_duration)
        bucketSort_duration_list.append(bucketSort_duration)
        timSort_duration_list.append(timSort_duration)

        length_lists.append(length_list)

    plot.getLineGraph(length_lists, quickSort_duration_list, "quick sort")
    plot.getLineGraph(length_lists, heapSort_duration_list, "heap sort")
    plot.getLineGraph(length_lists, mergeSort_duration_list, "merge sort")
    plot.getLineGraph(length_lists, radixSort_duration_list, "radix sort")
    plot.getLineGraph(length_lists, bucketSort_duration_list, "bucket sort")
    plot.getLineGraph(length_lists, timSort_duration_list, "tim sort")


generateGraph()



