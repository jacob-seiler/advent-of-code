from pathlib import Path

path = (Path(__file__).parent / "./q3.txt").resolve()

data = []

with open(path) as f:
    for line in f:
        data.append(line.strip())

gamma = [0] * 12
epsilon = [0] * 12

for bits in data:
    for i, bit in enumerate(bits):
        gamma[i] += 1 if bit == "1" else -1

for i, bit in enumerate(gamma):
    gamma[i] = "1" if bit > 0 else "0"
    epsilon[i] = "1" if bit <= 0 else "0"

gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)
print(gamma * epsilon)