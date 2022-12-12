from pathlib import Path

path = (Path(__file__).parent / "./q18.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        data.append(line)

# Part A
def new_total(total, val, op):
    if op == None:
        total = val
    elif op == "+":
        total += val
    elif op == "*":
        total *= val

    return total

def calc_expression(line):
    depth = [0]
    op = [None]
    index = 0

    for char in line:
        if char == " ":
            continue

        if char == "+" or char == "*":
            op[index] = char
            continue

        if char == "(":
            index += 1
            
            if len(depth) >= index:
                depth.append(0)
                op.append(None)
            
            continue

        val = None

        if char == ")":
            index -= 1
            op.pop()
            val = depth.pop()
        else:
            val = int(char)
        
        depth[index] = new_total(depth[index], val, op[index])

    return depth[0]

# Part B
def add_BEDMAS(line):
    new_line = [")"]

    for i in range(len(line) - 1, -1, -1):
        char = line[i]

        if char == "*":
            new_line.insert(0, ")*(")
            continue

        if char == "(" or char == ")":
            new_line.insert(0, char)
        
        new_line.insert(0, char)
    
    new_line.insert(0, "(")

    return ''.join(new_line)

total = 0
total2 = 0

for line in data:
    total += calc_expression(line)
    line = add_BEDMAS(line)
    total2 += calc_expression(line)

print(total)
print(total2)