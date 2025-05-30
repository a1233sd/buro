# Задача 2: минимальная подпоследовательность, содержащая алфавит
from collections import defaultdict

alphabet = set(range(1, 27))
with open("data_prog_contest_problem_2.txt") as f:
    lines = f.readlines()
    sequence = list(map(int, lines[1].strip().split()))

left = 0
min_len = float('inf')
window = None
count = defaultdict(int)
found = set()

for right in range(len(sequence)):
    val = sequence[right]
    if val in alphabet:
        count[val] += 1
        found.add(val)

    while alphabet.issubset(found):
        if right - left + 1 < min_len:
            min_len = right - left + 1
            window = (left, right)
        left_val = sequence[left]
        if left_val in alphabet:
            count[left_val] -= 1
            if count[left_val] == 0:
                found.remove(left_val)
        left += 1

print("Длина минимальной подпоследовательности:", min_len if window else "NONE")
