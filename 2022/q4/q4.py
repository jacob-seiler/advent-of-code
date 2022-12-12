from pathlib import Path

path = (Path(__file__).parent / "./q4.txt").resolve()

data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        assn1, assn2 = line.split(",")
        assn1 = [int(i) for i in assn1.split("-")]
        assn2 = [int(i) for i in assn2.split("-")]
        data.append((assn1, assn2))

# Part 1
def checkOverlap(assn1, assn2):
    return assn2[0] >= assn1[0] and assn2[1] <= assn1[1]

overlaps = 0

for pairs in data:
    assn1, assn2 = pairs
    
    if checkOverlap(assn1, assn2) or checkOverlap(assn2, assn1):
        overlaps += 1

print(overlaps)

# Part 2
def checkOverlap2(assn1, assn2):
    return (assn2[0] >= assn1[0] and assn2[0] <= assn1[1]) or (assn2[1] >= assn1[0] and assn2[1] <= assn1[1])

overlaps = 0

for pairs in data:
    assn1, assn2 = pairs
    
    if checkOverlap2(assn1, assn2) or checkOverlap2(assn2, assn1):
        overlaps += 1

print(overlaps)
