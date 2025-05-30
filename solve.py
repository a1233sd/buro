# Задача 3: Рекурсивная последовательность
f = [1, 3]
a = [1, 3]
while len(a) <= 40:
    next_val = 5 * f[-1] + f[-2]
    f.append(next_val)
    if next_val % 2 == 1:
        a.append(next_val)

print("A[39] =", a[39])
