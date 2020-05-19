A, B, C, X, Y = list(map(int, input().split()))
for num_c in range(0, 2 * max(X, Y) + 1, 2):
    num_a = X - num_c // 2 if X - num_c // 2 > 0 else 0
    num_b = Y - num_c // 2 if Y - num_c // 2 > 0 else 0
    if num_c == 0:
        min_money = A * num_a + B * num_b
    else:
        if (A * num_a + B * num_b + C * num_c) < min_money:
            min_money = A * num_a + B * num_b + C * num_c
print(min_money)
