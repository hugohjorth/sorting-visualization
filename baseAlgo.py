#swapping 2 elements position in an array
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

#A basic implementation of insertion sort
#using yield to "return" after each step
def insertSort(arr):
    n = len(arr)

    for i in range(1,n):
        value = arr[i]
        j = i-1
        while j >= 0 and value < arr[j]:

            arr[j+1] = arr[j]
            j -= 1

    
            arr[j+1] = value
            yield arr

    


#The partion algorithm
def partion(arr, start, end):
    pivot = arr[end]
    p_index = start
    for iter in range(start, end):
        if arr[iter] <= pivot:
            arr[p_index], arr[iter] = arr[iter], arr[p_index]
            p_index += 1
    
    arr[p_index], arr[end] = pivot, arr[p_index]
    return p_index
#The main Quick Sort algorithm
#TODO implement step through functionality
def quickSort(arr, start, end):
    if start < end:
        pivot = partion(arr, start, end) 
        quickSort(arr, start, pivot-1)
        quickSort(arr, pivot+1, end)


#test = [9,5,3,10,2,12]
#print(quickSort(test, 0, len(test)-1))
#print(test)


