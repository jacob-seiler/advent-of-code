from pathlib import Path

path = (Path(__file__).parent / "./q7.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        data.append(line)

directory = dict()
level = ""

outputting = False

for line in data:
    if line[0] == "$":
        outputting = False
        if line[2] == 'c':
            arg = line.split(" ")[2]
            
            if arg == "/":
                level = ""
            elif arg == "..":
                level = '/'.join(level.split("/")[:-1])

                if len(level) > 0 and level[0] == "/":
                    level = level[1:]
            else:
                if level == "":
                    level += arg
                else:
                    level += "/" + arg
        else:
            outputting = True
            continue

    if outputting:
        if line[0] == "d":
            continue

        val = int(line.split(" ")[0])
        temp = level.split("/")
        if temp[0] != "":
            temp.insert(0, "")

        for i in range(len(temp)):
            dir = '/'.join(temp[:i + 1])

            if dir not in directory:
                directory[dir] = 0

            directory[dir] += val

# Part A
total = 0

for d in directory:
    v = directory[d]

    if v <= 100000:
        total += v
    
print(total)

# Part B
total = 70000000
need = 30000000
used = directory[""]
rem = total - used
smallest = None

for d in directory:
    v = directory[d]

    if rem + v < need:
        continue

    if smallest == None or smallest > v:
        smallest = v

print(smallest)