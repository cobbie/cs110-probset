from collections import deque

def plugin(s):
    # stack for characters to check
    string_stack = deque()

    # input string in a list
    arr_s = [c for c in s]

    # for each character, append to stack. if the last two are equal, pop both
    for c in arr_s:
        string_stack.append(c)
        if len(string_stack) > 1:
            if string_stack[-1] == string_stack[-2]:
                string_stack.pop()
                string_stack.pop()
    return ''.join(string_stack)

print(plugin(input()))