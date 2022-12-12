from pathlib import Path

path = (Path(__file__).parent / "./q9.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = int(line.strip())
        data.append(line)

def get_all_sums(data):
    sums = set()

    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue

            sums.add(data[i] + data[j])

    return sums

# Part A
ans = 0

for i, num in enumerate(data):
    if i < 25:
        continue

    prev_25 = data[i - 25:i]
    if data[i] not in get_all_sums(prev_25):
        ans = data[i]
        break

print(ans)

# Part B
ans2 = None
for i, num in enumerate(data):
    if i == 0:
        continue

    for j in range(i):
        prevs = data[j:i + 1]

        if len(prevs) < 2:
            break

        if sum(prevs) == ans:
            ans2 = max(prevs) + min(prevs)
            break

        if ans2 != None:
            break

print(ans2)
