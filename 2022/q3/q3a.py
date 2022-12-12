from pathlib import Path

path = (Path(__file__).parent / "./q3.txt").resolve()

def findSame(first, second):
    com_str = ''.join(set(first).intersection(second))
    return com_str[0]

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
    for line in f:
        rucksack = line.strip()
        comp1 = rucksack[:len(rucksack) // 2]
        comp2= rucksack[len(rucksack) // 2:]

        char = findSame(comp1, comp2)
        priority = calcPriority(char)
        
        total += priority

print(total)