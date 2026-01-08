def bubble_sort(arr: list[int]) -> list[int]:
    last_unsorted_index = len(arr) -1
    solved = False
    while not solved:
        solved = True
        for i in range(last_unsorted_index):
            if arr[i] > arr[i+1]:
                solved = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
        last_unsorted_index -= 1

    return arr


main_input = bubble_sort(list(map(int, input().split())))
print(main_input)
