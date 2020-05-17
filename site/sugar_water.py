A, B, C, D, E, F = list(map(int, input().split()))

max_concentration = 0
max_sugar = 0
max_sugar_water = 0
for a in range(F // (100 * A) + 1):
    for b in range((F - 100 * A * a) // (100 * B) + 1):
        for c in range(E * (a * A + b * B) // C + 1):
            d = (E * (a * A + b * B) - c * C) // D
            tmp_sugar = c * C + d * D
            if tmp_sugar > E * (a * A + b * B):
                continue
            tmp_sugar_water = a * 100 * A + b * 100 * B + c * C + d * D
            if tmp_sugar_water > F or tmp_sugar_water == 0:
                continue
            tmp_concentration = tmp_sugar / tmp_sugar_water
            print(tmp_sugar_water, tmp_sugar, tmp_concentration)
            if max_concentration < tmp_concentration:
                max_concentration = tmp_concentration
                max_sugar_water = tmp_sugar_water
                max_sugar = tmp_sugar
print(max_sugar_water, max_sugar)
