# coding utf-8
"""
1<=n<=100
1<=wi, vi<=100
1<=W<=10000
"""

import numpy as np

n = int(input())
w = list(input())
v = list(input())
W = int(input())

if __name__ == "__main__":
    dp = np.zeros((n + 1, W + 1))
    for i in range(n):
        for sum_w in range(W + 1):
            if sum_w - w[i] >= 0:
                dp[i + 1][sum_w] = max(dp[i][sum_w], dp[i][sum_w - w[i]] + v[i])
            else:
                dp[i + 1][sum_w] = dp[i][sum_w]
