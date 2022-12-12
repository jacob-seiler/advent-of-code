from pathlib import Path

path = (Path(__file__).parent / "./q8.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip().split()
        line[1] = int(line[1][1:]) * int((1 if line[1][0] == "+" else -1))
        data.append(line)

def execute(data):
    ran = set()
    index = 0
    accum = 0
    halted = True

    while index < len(data):
        if index in ran:
            halted = False
            break

        ran.add(index)

        inst, val = data[index]

        if inst == "nop":
            index += 1
            continue

        if inst == "acc":
            accum += val
            index += 1
            continue

        if inst == "jmp":
            index += val
            continue
    
    return accum, halted

# Part A
accum, halted = execute(data)
print(accum)

# Part B
for i in range(len(data)):
    temp = data.copy()
    inst, val = temp[i]

    if inst == "acc":
        continue

    if inst == "nop":
        temp[i] = "jmp", val
    else:
        temp[i] = "nop", val

    accum, halted = execute(temp)
    
    if halted:
        break

print(accum)
