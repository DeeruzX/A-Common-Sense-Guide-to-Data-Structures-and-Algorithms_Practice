def duplicate_check(arr: list[int]) -> bool:
    return len(arr) != len(set(arr))


main_input = duplicate_check(list(map(int, input().split())))
print(main_input)
