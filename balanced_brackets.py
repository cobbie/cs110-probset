from collections import deque

def determine_balanced(s):
    if len(s) % 2 != 0:
        return 'NO'
    prob_stack = deque()
    matching_dict = {'{': '}', '[': ']', '(': ')'}
    opening = list(matching_dict.keys())
    closing = list(matching_dict.values())
    arr_s = [c for c in s]
    if arr_s[0] in closing:
        return 'NO'
    for ind, c in enumerate(arr_s):
        prob_stack.append(c)
        if c in closing and len(prob_stack) > 1:
            prob_stack.pop()
            if matching_dict[prob_stack.pop()] != c:
                return 'NO'
        elif c in closing and len(prob_stack) == 1 or ind == len(arr_s)-1 and c in opening:
            return 'NO'

    return 'YES'

num_ins = int(input())
ans_arr = []
for s in range(num_ins):
    input_s = input()
    ans_arr.append(determine_balanced(input_s))
print(*ans_arr, sep='\n')