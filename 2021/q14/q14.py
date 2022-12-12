from pathlib import Path

path = (Path(__file__).parent / "./q14.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        data.append(line)

polymer = data[0]
rules = dict()

for line in data:
    if "->" not in line:
        continue

    key, value = line.split(" -> ")
    rules[key] = value

# Part A
# STEPS = 10

# for step in range(STEPS):
#     print("step", step + 1)
#     new_polymer = [polymer[-1]]

#     for i in range(len(polymer) - 1, 0, -1):
#         right = polymer[i]
#         left = polymer[i - 1]
#         key = left + right
        
#         if key in rules:
#             new_polymer.append(rules[key])

#         new_polymer.append(left)
    
#     polymer = ''.join(new_polymer[::-1])

# # Find most and least common element
# import collections
# from collections import Counter
# res = Counter(polymer)
# res = min(res, key = res.get)
# print(collections.Counter(polymer).most_common(1)[0][1] - polymer.count(res))

# Part B
STEPS = 40
pairs = {}

# Setup
for i in range(len(polymer) - 1):
    key = polymer[i] + polymer[i + 1]
    
    if key not in pairs:
        pairs[key] = 0

    pairs[key] += 1

# Run
for step in range(STEPS):
    old_pairs = pairs.copy()

    for pair in old_pairs:
        if pair not in rules:
            continue

        count = old_pairs[pair]
        key = rules[pair]
        
        pairs[pair] -= count

        new_l = pair[0] + key
        new_r = key + pair[1]

        if new_l not in pairs:
            pairs[new_l] = 0
        
        if new_r not in pairs:
            pairs[new_r] = 0

        pairs[new_l] += count
        pairs[new_r] += count

    old_pairs = pairs.copy()

    for pair in old_pairs:
        if pairs[pair] == 0:
            del pairs[pair]

# Get largest and smallest
char_occurences = dict()

for pair in pairs:
    count = pairs[pair]

    for char in pair:
        if char not in char_occurences:
            char_occurences[char] = 0

        char_occurences[char] += count

largest = None
smallest = None

for char in char_occurences:
    value = char_occurences[char]
    
    if largest == None or char_occurences[largest] < value:
        largest = char

    if smallest == None or char_occurences[smallest] > value:
        smallest = char

print((char_occurences[largest] - char_occurences[smallest]) // 2)