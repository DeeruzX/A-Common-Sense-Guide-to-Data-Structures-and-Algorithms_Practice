def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        lowest_index = i
        for x in range(i+1, len(arr)):
            print(arr)
            if arr[x] < arr[lowest_index]:
                lowest_index = x

        if lowest_index != i:
            arr[i], arr[lowest_index] = arr[lowest_index], arr[i]
    return arr


main_input = selection_sort(list(map(int, input().split())))
print(main_input)
