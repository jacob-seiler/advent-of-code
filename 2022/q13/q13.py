from pathlib import Path
import json

path = (Path(__file__).parent / "./q13.txt").resolve()
data = []
index = 0

with open(path) as f:
    for line in f:
        line = line.strip()
        if line == "":
            index += 1
            continue

        if index >= len(data):
            data.append([])
        
        data[index].append(json.loads(line))

def is_valid(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return True

        if left > right:
            return False

        return None

    if type(left) == list and type(right) == list:
        i = 0

        while i < len(left) and i < len(right):
            res = is_valid(left[i], right[i])

            if res != None:
                return res

            i += 1

        if i == len(left) and i != len(right):
            return True
        
        if i != len(left) and i == len(right):
            return False

        return None

    if type(left) == int:
        return is_valid([left], right)

    return is_valid(left, [right])

correct = 0

for i, pair in enumerate(data):
    left, right = pair
    val = is_valid(left, right)

    if val == True:
        correct += i + 1

print(correct)

lines = [[[2]], [[6]]]

for pair in data:
    left, right = pair
    lines.append(left)
    lines.append(right)

def sort(arr):
    n = len(arr)
    
    swapped = False
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if not is_valid(arr[j], arr[j + 1]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return

sort(lines)

index2 = None
index6 = None

for i, line in enumerate(lines):
    if line == [[2]]:
        index2 = i + 1

    if line == [[6]]:
        index6 = i + 1

    if index2 != None and index6 != None:
        break

print(index2 * index6)