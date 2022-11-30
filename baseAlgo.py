import math

#swapping 2 elements position in an array
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

#A basic implementation of insertion sort
#That has been modified to only run one iteration at a time
def insertSort(arr,n):
    i=n
    while len(arr) > i:

        key = arr[i]

        j =i-1

        while j >= 0 and key < arr[j]:

            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = key
        return arr
        

#The partion algorithm
def partion(arr, low, high):
    pivot = arr[high]

    i = low-1

    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]

        
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    return i+1

#The main Quick Sort algorithm
#TODO implement step through functionality
def quickSort(arr, low, high):
    if low < high:
        pivot = partion(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)

# test = [9,5,3,10,2,12]
# print(quickSort(test, 0, len(test)-1))
# print(test)
#median of three - one of the better pivot selector for Quick Sort
def medianOfThree(arr):
    middle = math.floor(len(arr)/2)
    temp = [arr[0], middle, arr[len(arr)-1]]
    temp.sort()
    return temp[1]    

