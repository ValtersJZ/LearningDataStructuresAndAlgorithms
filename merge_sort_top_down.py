def merge_sort_td(ls):
    """
    Top down merge sort algorithm (divide and conquer sorter)
    Time: O(nlog(n)); Auxiliary space: O(n)

    Notes: This implementation works, because in python lists
    are mutable and are thus passed by reference and not copied
    to a new local object within the function implicitly (e.g.
    unlike tuples). This also means that the return is
    unnecessary as the original list is changed in the process.
    For more details search the internet.
    """
    if len(ls) > 1:
        centre = len(ls)//2
        left_half = ls[:centre]
        right_half = ls[centre:]

        # break down recursively
        merge_sort_td(left_half)
        merge_sort_td(right_half)

        # combine
        left = 0    # left array iteration index
        right = 0   # right array iteration index
        i = 0       # merged array iteration index

        # merge arrays while both indices are in their array ranges
        while left < len(left_half) and right < len(right_half):
            # If left is smaller add it to sorted array
            if left_half[left] < right_half[right]:
                ls[i] = left_half[left]
                left += 1

            # If right is smaller and it to sorted array
            else: # right_half[right] <= left_half[left]:
                ls[i] = right_half[right]
                right += 1
            i += 1

        # Merge what is left
        # Left: merge if it left_arr has more elements
        while left < len(left_half):
            ls[i] = left_half[left]
            i += 1
            left += 1

        # Right: merge if it right_arr has more elements
        while right < len(right_half):
            ls[i] = right_half[right]
            i += 1
            right += 1

    return ls


if __name__ == "__main__":
    from random import randrange
    my_list = [randrange(0,100) for i in range(10)]
    print("Original:\t {}".format(my_list))
    print("Sorted:\t\t {}".format(merge_sort_td(my_list)))
    # print(my_list)
