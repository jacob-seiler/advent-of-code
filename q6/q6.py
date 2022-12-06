from pathlib import Path

path = (Path(__file__).parent / "./q6.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        data = line

def findSpot():
    for i in range(3, len(data)):
        seen = set([data[i - 3], data[i - 2], data[i - 1], data[i]])
        if len(seen) == 4:
            return i + 1

    return None

print(findSpot())

def findSpot2():
    for i in range(14, len(data)):
        seen = set([data[i - 13], data[i - 12], data[i - 11], data[i - 10], data[i - 9], data[i - 8], data[i - 7], data[i - 6], data[i - 5], data[i - 4], data[i - 3], data[i - 2], data[i - 1], data[i]])
        if len(seen) == 14:
            return i + 1

    return None

print(findSpot2())