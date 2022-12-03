from pathlib import Path

path = (Path(__file__).parent / "./q1.txt").resolve()
elves = []

with open(path) as f:
    elfIndex = 0

    for line in f:
        if line == "\n":
            elfIndex += 1
            continue

        if len(elves) <= elfIndex:
            elves.append(0)
        
        cals = int(line[:-1])
        elves[elfIndex] += cals

first = max(elves)
print(first)

# Part B
elves.remove(first)

second = max(elves)
elves.remove(second)

third = max(elves)
elves.remove(third)

print(first + second + third)