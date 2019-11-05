from collections import deque

def get_largest_rectangle(arr_h):

    stack = deque()
    stack.append(-1)
    current_max = 0
    
    for i in range(len(arr_h)):
        while stack[-1] != -1 and arr_h[stack[-1]] >= arr_h[i]:
            last = stack.pop()
            # area = min(stack) * len(stack)
            area = arr_h[last]*(i - stack[-1]-1)
            if area > current_max:
                current_max = area
        stack.append(i)

    while stack[-1] != -1:
        last = stack.pop()
        area = arr_h[last] * (len(arr_h) - stack[-1] - 1)
        if area > current_max:
            current_max = area
    return current_max

in_1 = int(input())
arr = [int(i) for i in input().split()]
print(get_largest_rectangle(arr))