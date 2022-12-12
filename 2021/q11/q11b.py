from pathlib import Path

path = (Path(__file__).parent / "./q11.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        data.append([int(i) for i in line])

steps = 0
total = 0

def is_zeros(data):
    for row in data:
        for octopus in row:
            if octopus != 0:
                return False

    return True

while not is_zeros(data):
    steps += 1
    flash_count = 0
    flashes = []
    flashed = set()

    for row in range(len(data)):
        for col in range(len(data[row])):
            data[row][col] += 1

            if data[row][col] > 9:
                flashes.append((row, col))

    while len(flashes) > 0:
        coords = flashes.pop()
        row, col = coords

        if coords in flashed:
            continue

        data[row][col] = 0
        flash_count += 1

        # Increment adjacent octopuses
        for i_row in range(-1, 2):
            for i_col in range(-1, 2):
                r = row + i_row
                c = col + i_col

                if r == row and c == col:
                    continue

                if 0 > r or r >= len(data):
                    continue

                if 0 > c or c >= len(data[row]):
                    continue

                if (r, c) in flashed:
                    continue

                data[r][c] += 1

                if data[r][c] > 9:
                    flashes.append((r, c))

        flashed.add(coords)
    
    total += flash_count

print(steps)