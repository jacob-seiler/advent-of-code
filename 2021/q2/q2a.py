from pathlib import Path

path = (Path(__file__).parent / "./q2.txt").resolve()

x = 0
y = 0

with open(path) as f:
    for line in f:
        op, val = line.strip().split(" ")
        val = int(val)

        if op == "forward":
            x += val
            continue

        if op == "up":
            y -= val
            continue

        y += val

print(x * y)