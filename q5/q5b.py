from pathlib import Path

path = (Path(__file__).parent / "./q5.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        data.append(line)

piles = [[], [], [], [], [], [], [], [], []]

for line in data:
    if line[:2] == " 1":
        break

    for i, x in enumerate(range(0, len(line), 4)):
        val = line[x + 1]
        
        if val == " ":
            continue
        
        piles[i].append(val)

print(piles)

skip = True
temp = []

for line in data:
    if line[:2] == " 1":
        skip = False
        continue

    if skip:
        continue

    temp.append(line.strip())

data = temp[1:]

for line in data:
    amount = int(line.split(" ")[1])
    start = int(line.split(" ")[3])
    end = int(line.split(" ")[5])

    temp = piles[start - 1][:amount]
    piles[start - 1] = piles[start - 1][amount:]
    
    for p in temp[::-1]:
        piles[end - 1].insert(0, p)

for pile in piles:
    if len(pile) > 0:
        print(pile[0], end="")

print("")