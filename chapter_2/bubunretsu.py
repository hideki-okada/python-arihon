# -*- coding: <encoding name> -*-

import numpy as np

n = int(input())
m = int(input())
s = str(input())
t = str(input())
dp = np.zeros((n + 1, m + 1))


# dp[i, j]をsのi番目までの文字列とtのj番目までの文字列の共通部分列の長さとする
# dp[i+1, j+1]はs[i+1] == t[j+1]ならdp[i, j] + 1、それ以外ならdp[i+1, j]とdp[i, j+1]の大きい方


for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i + 1, j + 1] = dp[i, j] + 1
        else:
            dp[i + 1, j + 1] = max(dp[i + 1, j], dp[i, j + 1])

print(dp[n, m])
