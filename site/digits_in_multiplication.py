import numpy as np

N = int(input())
min_keta = 10 ** 6


def get_keta(var):
    ans = 0
    while True:
        var = var // 10
        ans += 1
        if var == 0:
            break
    return ans


for a in range(1, int(np.sqrt(N)) + 1):
    if N % a == 0:
        tmp_keta = get_keta(max(a, N // a))
        if tmp_keta < min_keta:
            min_keta = tmp_keta
print(min_keta)
