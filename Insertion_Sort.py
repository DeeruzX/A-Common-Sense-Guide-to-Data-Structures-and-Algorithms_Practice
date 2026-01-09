def insertion_sort(arr: list[int]) -> list[int]:
    temp = 1
    is_sorted = False
    while not is_sorted and temp != len(arr):
        is_sorted = True
        for i in range(temp):
            if arr[temp] < arr[i]:
                is_sorted = False
                arr[temp], arr[i] = arr[i], arr[temp]
        temp += 1

    return arr


main_input = insertion_sort(list(map(int, input().split())))
print(main_input)
