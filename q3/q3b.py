from pathlib import Path

path = (Path(__file__).parent / "./q3.txt").resolve()

def findSame(first, second, third):
    temp = set(first).intersection(second)
    com_str = ''.join(temp.intersection(third))
    return com_str

def calcPriority(char):
    ascii = int(ord(char))
    val = ascii - 64

    if val <= 26:
        val += 26
    else:
        val -= 32

    return val

total = 0

with open(path) as f:
    group = []
    for line in f:
        print(line.strip())
        group.append(line.strip())

        if len(group) == 3:
            char = findSame(*group)
            total += calcPriority(char)
            group = []

print(total)