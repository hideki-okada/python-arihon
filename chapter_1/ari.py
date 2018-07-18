import numpy as np
L = input()
n = input()
x = map(int, raw_input().split())
min = 0
max = 0
for i in range(n):
    t_min = 0
    t_max = 0
    if x[i]< L/2.0:
        t_min = x[i]
        t_max = L-x[i]
    else:
        t_min = L-x[i]
        t_max = x[i]
    if t_min > min:
        min = t_min
    if t_max > max:
        max = t_max
print min,max

        
