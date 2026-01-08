def binary_search(arr: list[int], target: int) -> int:
    index_x = 0
    index_y = len(arr) - 1
    while True and target in arr:
        print(arr[index_x:index_y + 1])

        mid_point = int((index_x + index_y) / 2)

        pointer_value = arr[mid_point]

        if pointer_value > target:
            index_y = mid_point - 1
        elif pointer_value < target:
            index_x = mid_point + 1
        elif pointer_value == target:
            return target
    return -1




main_input = binary_search(list(map(int, input().split())), int(input()))

print(main_input)
