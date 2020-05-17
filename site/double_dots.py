from collections import deque

import numpy as np

N, M = list(map(int, input().split()))
tsuro = [list(map(int, input().split())) for _ in range(M)]
tsuro = np.array(tsuro)
arr = list(range(2, N + 1))
tsuro = np.sort(tsuro, axis=1)
order = np.argsort(tsuro[:, 0])
tsuro = tsuro[order]
print(tsuro)
depth_array = np.ones(N) * -1
depth_array[0] = 0
ans_array = np.zeros(N)
tsuro_queue = deque(tsuro.tolist())
counts = 0
while tsuro:
    if counts > 2 * N:
        break
    room_a, room_b = tsuro.popleft()
    room_a, room_b = room_a - 1, room_b - 1
    if depth_array[room_a] != -1 and depth_array[room_b] != -1:
        continue
    elif depth_array[room_a] != -1:
        depth_array[room_b] = depth_array[room_a] + 1
        ans_array[room_b] = room_a + 1
        tsuro.append()
    elif depth_array[room_b] != -1:
        depth_array[room_a] = depth_array[room_b] + 1
        ans_array[room_a] = room_b + 1
    else:
        tsuro.append([room_a + 1, room_b + 1])
    counts += 1
print(depth_array[depth_array != -1])
if -1 not in depth_array:
    print('Yes')
    for ans in ans_array[1:]:
        print(int(ans))
else:
    print('No')
