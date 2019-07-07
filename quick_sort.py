"""
Simple quick sort implementation.
(There are better ways to write it)

Time: Qavg(nlog(n)) and it exhibits spatial locality
and thus cache memory speeds it up. Qworst_case: O(n^2)
(like bubble sort), wost case occurs when the list
is already partially sorted.
Auxiliary space: O(1)
"""

def partition(array, first, last):
    low = first + 1
    high = last
    pivot = array[first]

    done = False
    while not done:
        while low <= high and array[low] <= pivot:
            low += 1
        while low <= high and array[high] >= pivot:
            high -= 1
        if low > high:
            done = True
        else:
            array[low], array[high] = array[high], array[low]

    array[first], array[high] = array[high], array[first]
    return high

def quick_sort(array, low, high):
    if low < high:
        p = partition(array, low, high)

        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)


def quicksort(array):
    quick_sort(array, 0, len(array) - 1)
    return array

if __name__ == "__main__":
    test = [21, 1, 3, 9, 25, 6, 14]
    print(test)
    print(quicksort(test))