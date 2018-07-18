import numpy as np

n = input()
a = map(int,raw_input().split())

a = np.array(a)
a = a[::-1]
#print a
sum = 0
for i in range(n-2):
    if a[i]<a[i+1]+a[i+2]:
        sum =  a[i]+a[i+1]+a[i+2]
        break
print sum
