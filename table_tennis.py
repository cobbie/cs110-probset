from copy import copy
from collections import deque

in_1 = input().split()
n = int(in_1[0])
k = int(in_1[1])
in_2 = input().split()

current_player = int(in_2[0])
current_opponent = int(in_2[1])
enemy_q = deque()
current_wins = 0
if n > 2:
    # Add all other enemies to the enemy queue (line)
    for i in in_2[2:]:
        enemy_q.appendleft(int(i))

    # Keep playing until a player wins k times
    while current_wins < k:

        # if current player wins, add current opponent to enemy queue, increase
        # win count by 1, and get next in line opponent as current opponent
        if current_player > current_opponent:
            enemy_q.appendleft(current_opponent)
            current_wins += 1
            current_opponent = enemy_q.pop()
            
            # for time limits: if opponent has beaten everyone already, stop the loop
            # and return the current player as the inevitable winner
            if current_wins > n - 1:
                break
            

        # if opponent wins, add current player to enemy queue, convert current opponent
        # to current player, change win count to one, and get next in line opponent as current opponent
        else:
            winner = copy(current_opponent)
            enemy_q.appendleft(current_player)
            current_player = winner
            current_wins = 1
            current_opponent = enemy_q.pop()

# if there are only two players, the higher power player will automatically win.
else:
    if current_player<current_opponent:
        current_player = current_opponent
    
print(current_player)