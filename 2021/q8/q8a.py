from pathlib import Path

path = (Path(__file__).parent / "./q8.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        
        sigs, outs = line.split(" | ")
        sigs = sigs.split(" ")
        outs = outs.split(" ")

        data.append({"signals": sigs, "outputs": outs})

total = 0

for line in data:
    outs = line["outputs"]

    for out in outs:
        if len(out) == 2 or len(out) == 4 or len(out) == 3 or len(out) == 7:
            total += 1

print(total)