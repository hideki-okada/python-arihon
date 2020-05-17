A, B, C, D, E, F = list(map(int, input().split()))

max_concentration = 0
max_sugar = 0
max_sugar_water = 0
for a in range(31):
    if a * 100 * A > F:
        continue
    for b in range(31):
        if 100 * A * a + 100 * B * b > F:
            continue
        for c in range(3000 // C + 1):
            if E * (a * A + b * B) < c * C:
                continue
            if 100 * A * a + 100 * B * b + c * C > F:
                continue
            # 濃度最大化のd
            d = (E * (a * A + b * B) - c * C) // D
            tmp_sugar_water = a * 100 * A + b * 100 * B + c * C + d * D
            if tmp_sugar_water == 0:
                continue
            if tmp_sugar_water > F:
                # 総量はFまでなのでdを調整
                d = (F - (a * 100 * A + b * 100 * B + c * C)) // D
            tmp_sugar_water = a * 100 * A + b * 100 * B + c * C + d * D
            tmp_sugar = c * C + d * D
            tmp_concentration = tmp_sugar / tmp_sugar_water
            if max_concentration <= tmp_concentration:
                max_concentration = tmp_concentration
                max_sugar_water = tmp_sugar_water
                max_sugar = tmp_sugar
print(max_sugar_water, max_sugar)
