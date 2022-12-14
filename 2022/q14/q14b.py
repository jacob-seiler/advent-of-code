from pathlib import Path

path = (Path(__file__).parent / "./q14.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip().split(" -> ")
        line = [[int(i.split(",")[0]), int(i.split(",")[1])] for i in line]
        data.append(line)

rocks = set()
lowest = 0

for line in data:
    curr_x, curr_y = line[0]
    rocks.add(tuple([curr_x, curr_y]))
    lowest = max(curr_y, lowest)

    for pos in range(1, len(line)):
        x, y = line[pos]

        while curr_x != x or curr_y != y:
            diff_x = x - curr_x
            diff_y = y - curr_y

            dir_x = diff_x // abs(diff_x) if diff_x != 0 else 0
            dir_y = diff_y // abs(diff_y) if diff_y != 0 else 0

            curr_x += dir_x
            curr_y += dir_y

            lowest = max(curr_y, lowest)
            rocks.add(tuple([curr_x, curr_y]))

lowest += 2
sands = set()

while True:
    sand_x = 500
    sand_y = 0

    while True:
        down = (sand_x, sand_y + 1)
        
        if down[1] != lowest and down not in rocks and down not in sands:
            sand_y += 1
            continue

        left = (sand_x - 1, sand_y + 1)

        if left[1] != lowest and left not in rocks and left not in sands:
            sand_x -= 1
            sand_y += 1
            continue

        right = (sand_x + 1, sand_y + 1)

        if right[1] != lowest and right not in rocks and right not in sands:
            sand_x += 1
            sand_y += 1
            continue

        sands.add((sand_x, sand_y))
        break

    if sand_x == 500 and sand_y == 0:
        break

print(len(sands))