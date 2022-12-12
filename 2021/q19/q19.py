from pathlib import Path

path = (Path(__file__).parent / "./q19.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        data.append(line)

for line in data:
    print(line)
