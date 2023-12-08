import math

lines = open('q8.txt').read().strip().split("\n")
instructions = lines[0]
nodes = {line.split(' = ')[0]:tuple(line.split(' = ')[1][1:-1].split(', ')) for line in lines[2:]}

# Part 1
curr = 'AAA'
steps = 0

while curr != 'ZZZ':
    for dir in instructions:
        value = nodes[curr]
        curr = value[0 if dir == 'L' else 1]
        steps += 1

print(steps)

# Part 2
currs = [node for node in nodes if node[-1] == 'A']
steps = [0 for _ in currs]

for i, curr in enumerate(currs):
    while curr[-1] != 'Z':
        steps[i] += 1

        for dir in instructions:
            value = nodes[curr]
            curr = value[0 if dir == 'L' else 1]


iterations = [x for x in steps]
print(math.lcm(*iterations) * len(instructions))
