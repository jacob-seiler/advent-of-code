from pathlib import Path

path = (Path(__file__).parent / "./q7.txt").resolve()
crabs = []

with open(path) as f:
    for line in f:
        line = line.strip()
        crabs = [int(i) for i in line.split(",")]

largest = max(crabs)
smallest = min(crabs)

# Part 1
pos = None
fuel = None

for i in range(smallest, largest + 1):
    fuel_total = 0

    for crab in crabs:
        fuel_total += abs(crab - i)

    if fuel == None or fuel > fuel_total:
        fuel = fuel_total
        pos = i

print(pos, fuel)

# Part 2
pos = None
fuel = None

for i in range(smallest, largest + 1):
    fuel_total = 0

    for crab in crabs:
        dist = abs(crab - i)
        sum = dist * (dist + 1) // 2
        fuel_total += sum

    if fuel == None or fuel > fuel_total:
        fuel = fuel_total
        pos = i

print(pos, fuel)