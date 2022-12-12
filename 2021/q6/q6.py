from pathlib import Path

path = (Path(__file__).parent / "./q6.txt").resolve()
habitat = [0] * 9

with open(path) as f:
    for line in f:
        fish = [int(i) for i in line.strip().split(",")]

        for i in fish:
            habitat[i] += 1

def run(days, habitat):
    for _ in range(days):
        temp = habitat[0]
        for i in range(8):
            habitat[i] = habitat[i + 1]
        
        habitat[8] = temp
        habitat[6] += temp

# Part 1
run(80, habitat)
print(sum(habitat))

# Part 2
run(256 - 80, habitat)
print(sum(habitat))