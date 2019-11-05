
from collections import deque

def shell(cmds):
    wd = deque()
    wd.append('/')
    arr_ans = []
    for cmd in cmds:
        if cmd == 'pwd':
            arr_ans.append(''.join(wd))
        elif cmd[:2]=='cd':
            path = cmd.split()[1]
            path_arr = path.split('/')
            for p in path_arr:
                if p =='':
                    wd.clear()
                    wd.append('/')
                elif p == '..':
                    wd.pop()
                else:
                    wd.append(p + '/')
    return arr_ans

in_1 = int(input())
arr_ins=[]
for cmd in range(in_1):
    arr_ins.append(input())
print(*shell(arr_ins),sep="\n")