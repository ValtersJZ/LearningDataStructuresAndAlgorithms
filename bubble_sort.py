def bubble_sort(ls):
    """Bubble sort the simplest sorting algorithm"""
    size = len(ls)

    while size > 1:
        i = 0
        while i < size - 1:
            if ls[i] > ls[i+1]:
                temp = ls[i+1]
                ls[i+1] = ls[i]
                ls[i] = temp
            i += 1
        size -= 1

    return ls


if __name__ == "__main__":
    my_list = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print(my_list)
    print(bubble_sort(my_list))