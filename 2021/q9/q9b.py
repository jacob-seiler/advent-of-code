from pathlib import Path

path = (Path(__file__).parent / "./q9.txt").resolve()
map = []

with open(path) as f:
    for line in f:
        line = line.strip()
        map.append([int(i) for i in line])

points = []

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
            points.append((row, col))

def findBasinSize(row, col, checked=set(), total=0):
    point = (row, col)
    
    if point in checked:
        return 0

    checked.add(point)

    if map[row][col] == 9:
        return 0

    temp = 0

    if row > 0:
        temp += findBasinSize(row - 1, col, checked, total)

    if row < len(map) - 1:
        temp += findBasinSize(row + 1, col, checked, total)

    if col > 0:
        temp += findBasinSize(row , col - 1, checked, total)

    if col < len(map[row]) - 1:
        temp += findBasinSize(row, col + 1, checked, total)
    
    return temp + 1 + total

sizes = []

for row, col in points:
    point = map[row][col]
    sizes.append(findBasinSize(row, col))

sizes = sorted(sizes)
print(sizes[-1] * sizes[-2] * sizes[-3])
    