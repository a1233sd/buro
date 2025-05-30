# Задача 4: Обратная функция g(n)
def f(n):
    return int(str(n)[::-1])

def g(n):
    return f(f(n)) / n

unique = set()
for n in range(2, 1030):
    unique.add(g(n))

print("Количество уникальных значений функции g(n):", len(unique))
