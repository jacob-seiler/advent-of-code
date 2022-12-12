from pathlib import Path

path = (Path(__file__).parent / "./q11.txt").resolve()
monkeys = []

monkey = 0

with open(path) as f:
    for line in f:
        line = line.strip()

        if line == "":
            monkey += 1
            continue

        if len(monkeys) <= monkey:
            monkeys.append(dict())

        monkey_dict = monkeys[monkey]

        if line[0] == "S":
            monkey_dict["items"] = [int(i) for i in line.split(": ")[1].split(", ")]

        if line[0] == "O":
            monkey_dict["op"] = line[21]
            monkey_dict["op_val"] = line[23:]

        if line[0] == "T":
            monkey_dict["test"] = int(line[19:])

        if line[0] == "I" and line[3] == "t":
            monkey_dict["success"] = int(line[25:])

        if line[0] == "I" and line[3] == "f":
            monkey_dict["fail"] = int(line[25:])

ROUNDS = 10_000

inspects = [0] * len(monkeys)

tcd = 1
for m in monkeys:
    tcd *= m["test"]

for round in range(ROUNDS):
    print(round)

    for mi, m in enumerate(monkeys):
        for _ in range(len(m["items"])):
            i = m["items"].pop()

            inspects[mi] += 1

            if m["op"] == "+":
                i += i if m["op_val"] == "old" else int(m["op_val"])
            else:
                i *= i if m["op_val"] == "old" else int(m["op_val"])
            
            # i //= 3
            i %= tcd
            success = i % m["test"] == 0

            pass_to = m["success"] if success else m["fail"]
            monkeys[pass_to]["items"].insert(0, i)

largest = None
second = None

for mi, ic in enumerate(inspects):
    if largest == None:
        largest = mi
        continue

    if second == None:
        second = mi
        continue

    if ic > inspects[largest]:
        second = largest
        largest = mi
        continue

    if ic > inspects[second]:
        second = mi
        continue

print(inspects)
print(inspects[largest] * inspects[second])