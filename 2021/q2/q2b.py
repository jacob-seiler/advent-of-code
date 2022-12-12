from pathlib import Path

path = (Path(__file__).parent / "./q2.txt").resolve()

aim = 0
x = 0
y = 0

with open(path) as f:
    for line in f:
        op, val = line.strip().split(" ")
        val = int(val)

        if op == "forward":
            x += val
            y += aim * val
            continue

        if op == "up":
            aim -= val
            continue

        aim += val

print(x * y)