from pathlib import Path

path = (Path(__file__).parent / "./q13.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        data.append(line)

points = set()
instructions = []

width = 0
height = 0

for line in data:
    if line == "":
        continue

    if line[0] == "f":
        dir, amount = line.split(" ")[-1].split("=")
        instructions.append((dir, int(amount)))
        continue

    x, y = [int(i) for i in line.split(",")]
    width = max(width, x)
    height = max(height, y)
    points.add((y, x))

width += 1
height += 1

for i in instructions:
    dir, amount = i
    
    if dir == 'x':
        for col in range(amount):
            for row in range(height):
                inv = (row, width - col - 1)

                if inv in points:
                    points.add((row, col))
                    points.remove(inv)

        width = amount
        continue
    
    if dir == 'y':
        for col in range(width):
            for row in range(amount):
                inv = (height - row - 1, col)

                if inv in points:
                    points.add((row, col))
                    points.remove(inv)

        height = amount
        continue

# For part A solution, change above loop to break instead of continue
print(len(list(points)))

for row in range(height):
    for col in range(width):
        if (row, col) in points:
            print("# ", end="")
        else:
            print(". ", end="")
    
    print()