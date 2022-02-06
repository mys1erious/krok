import random
import time


def sort_inf(sort_type, array):
    print(sort_type.__name__ + ':')

    start_time = time.time()
    arr = sort_type(list.copy(array))
    print("execution time:", "%s seconds" % (time.time() - start_time))

    cmp = arr[1]
    swap = arr[2]
    print("Comparisons number:", cmp)
    print("Swaps number:", swap, '\n')
    return arr


def bubble_sort(array):

    cmpcount, swapcount = 0, 0
    flag = True
    i = 0

    while flag:
        flag = False
        for j in range(len(array)-1-i):
            cmpcount += 1
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapcount += 1
                flag = True
        i+=1

    return array, cmpcount, swapcount


def selection_sort(array):

    cmpcount, swapcount = 0, 0

    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            cmpcount+=1
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
        swapcount += 1

    return array, cmpcount, swapcount


def insertion_sort(array):

    cmpcount, swapcount = 0, 0

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            cmpcount += 1
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        swapcount += 1

    return array, cmpcount, swapcount


def cocktail_sort(array):

    cmpcount, swapcount = 0, 0
    flag = True
    i = 0
    while flag:
        flag = False
        for j in range(i, len(array)-1-i):
            cmpcount+=1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapcount += 1
                flag = True
        i+=1
        for j in range(len(array)-1-i, i-1, -1):
            cmpcount+=1
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                swapcount += 1
                flag = True

    return array, cmpcount, swapcount


def shell_sort(array):

    cmpcount, swapcount = 0, 0
    gap = len(array)//2

    while gap > 0:
        for i in range(gap, len(array)):
            key = array[i]
            j = i
            while j >= gap and key < array[j-gap]:
                cmpcount+=1
                array[j] = array[j-gap]
                swapcount += 1
                j = j-gap
            array[j] = key
        gap = gap//2

    return array, cmpcount, swapcount


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):

    cmpcount, swapcount = 0, 0
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)
        cmpcount += 1

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        swapcount+=1
        heapify(arr, i, 0)
        cmpcount += 1

    return arr, cmpcount, swapcount

check = input('Press "y" if u want to create ur array: ')
if check == 'y':
    size = int(input("Size of array: "))
    arr2 = [int(input(f"Elem {i+1}/{size}")) for i in range(size)]
    print('Entered arr', arr2)
    arr2 = insertion_sort(arr2)
    print('Sorted entered arr', arr2, '\n')


arr1 = [random.randint(1, 1000) for i in range(10000)]

bubble = sort_inf(bubble_sort, list.copy(arr1))
selection = sort_inf(selection_sort, list.copy(arr1))
insertion = sort_inf(insertion_sort, list.copy(arr1))
cocktail = sort_inf(cocktail_sort, list.copy(arr1))
shell = sort_inf(shell_sort, list.copy(arr1))
heap = sort_inf(heap_sort, list.copy(arr1))

print('Ascending sorted sort: ', heap)
print('Descending sorted sort: ', bubble)