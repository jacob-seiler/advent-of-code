from pathlib import Path

path = (Path(__file__).parent / "./q1.txt").resolve()

depths = []

with open(path) as f:
    for line in f:
        depths.append(int(line.strip()))

total = 0

for i in range(3, len(depths)):
    prev = depths[i - 3] + depths[i - 2] + depths[i - 1]
    curr = depths[i - 2] + depths[i - 1] + depths[i]
    
    if curr - prev > 0:
        total += 1

print(total)
