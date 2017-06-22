def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                temp = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = temp

    print(lst)
