from pathlib import Path

path = (Path(__file__).parent / "./template.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        data.append(line.strip())

for line in data:
    print(line)
