from pathlib import Path

path = (Path(__file__).parent / "./q9.txt").resolve()
map = []

with open(path) as f:
    for line in f:
        line = line.strip()
        map.append([int(i) for i in line])

risk_sum = 0

for row in range(len(map)):
    amount = len(map[row])

    for col in range(amount):
        point = map[row][col]

        checks = 0

        if row == 0 or map[row - 1][col] > point:
            checks += 1

        if row == len(map) - 1 or map[row + 1][col] > point:
            checks += 1

        if col == 0 or map[row][col - 1] > point:
            checks += 1

        if col == amount - 1 or map[row][col + 1] > point:
            checks += 1

        if checks == 4:
            risk_sum += 1 + point

print(risk_sum)