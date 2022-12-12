from pathlib import Path

path = (Path(__file__).parent / "./q10.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        data.append(int(line))

# Part A
data = sorted(data)
threes = 1
ones = 1

for i in range(1, len(data)):
    diff = data[i] - data[i - 1]

    if diff == 1:
        ones += 1
    else:
        threes += 1

print(threes * ones)

# Part B (doesn't work)
def num_ways(data, index):
    if index == 0:
        return 1
    
    if index == 1:
        return 1 + num_ways(data, index - 1)
    
    prev2 = data[index - 2]

    total = num_ways(data, index - 1)

    if data[index] - prev2 == 3:
        total += num_ways(data, index - 2)

    return total

print(num_ways(data, len(data) - 1))