#I might create a flinter later on...
def brackets_checker(main_input: str):
    open_brackets = ["(", "{", "["]
    close_brackets = [")", "}", "]"]
    matching_bracket = {")": "(", "}": "{", "]": "["}
    stack = []
    for i in main_input:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            if not stack or stack[-1] != matching_bracket[i]:
                return False
            stack.pop()
    return len(stack) == 0


print(brackets_checker(input()))
