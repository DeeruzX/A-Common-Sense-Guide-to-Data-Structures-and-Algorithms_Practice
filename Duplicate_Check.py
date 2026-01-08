def duplicate_check(arr: list[int]) -> bool:
    if len(arr) != len(set(arr)):
        return True
    else:
        return False


main_input = duplicate_check(list(map(int, input().split())))
print(main_input)
