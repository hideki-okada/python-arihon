# coding utf-8

"""
1<=n<=100
1<=wi, vi<=100
1<=W<=10000
"""

import numpy as np

n = int(input())
w = list(map(int, input().split()))
v = list(map(int, input().split()))
W = int(input())

if __name__ == "__main__":
    dp = np.zeros((n + 1, W + 1), dtype=np.uint32)
    for i in range(n):
        for sum_w in range(W + 1):
            if sum_w - w[i] < 0:
                dp[i + 1][sum_w] = dp[i][sum_w]
            else:
                dp[i + 1][sum_w] = max(dp[i][sum_w], dp[i + 1][sum_w - w[i]] + v[i])
    print(dp[-1, -1])
