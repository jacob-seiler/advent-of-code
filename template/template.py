from pathlib import Path

path = (Path(__file__).parent / "./template.txt").resolve()

with open(path) as f:
    for line in f:
        print(line.strip())
