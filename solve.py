# Задача 1: минимальное число точек, покрывающих все отрезки
segments = []
with open("data_prog_contest_problem_1.txt") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2:
            a, b = map(int, parts)
            segments.append((min(a, b), max(a, b)))

segments.sort(key=lambda x: x[1])
points = []
last_point = -1
for start, end in segments:
    if last_point < start:
        last_point = end
        points.append(last_point)

print("Минимальное число точек:", len(points))
