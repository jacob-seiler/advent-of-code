from pathlib import Path

path = (Path(__file__).parent / "./q12.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        data.append(line)

caves = {}
small_caves = set()

for line in data:
    cave1, cave2 = line.split("-")
    
    if cave1 not in caves:
        caves[cave1] = set()

    if cave2 not in caves:
        caves[cave2] = set()

    caves[cave1].add(cave2)
    caves[cave2].add(cave1)

    if cave1 == cave1.lower():
        small_caves.add(cave1)
    
    if cave2 == cave2.lower():
        small_caves.add(cave2)

# Part A
paths = set()
curr_paths = [["start"]]

while len(curr_paths) != 0:
    p = curr_paths.pop()
    node = p[-1]

    if node == "end":
        paths.add(tuple(p))
        continue

    connections = caves[node]

    for connection in connections:
        # Small caves can only be visited once!
        if connection == connection.lower() and connection in p:
            continue

        new_path = p.copy()
        new_path.append(connection)

        if new_path in curr_paths or tuple(new_path) in paths:
            continue

        curr_paths.insert(0, new_path)

print(len(paths))

# Part B
paths = set()
curr_paths = [["start"]]

while len(curr_paths) != 0:
    p = curr_paths.pop()
    node = p[-1]

    print(p, len(paths))

    if node == "end":
        paths.add(tuple(p))
        continue

    connections = caves[node]

    for connection in connections:
        # Small caves can only be visited once!
        if connection == connection.lower() and connection in p:
            if connection == "start":
                continue

            highest_count = 0

            for cave in small_caves:
                highest_count = max(highest_count, p.count(cave))

            if highest_count >= 2:
                continue

        new_path = p.copy()
        new_path.append(connection)

        if new_path in curr_paths or tuple(new_path) in paths:
            continue

        curr_paths.insert(0, new_path)

print(len(paths))
