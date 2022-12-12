# from pathlib import Path

# path = (Path(__file__).parent / "./q10.txt").resolve()
# data = []
# instructions = []

# with open(path) as f:
#     for line in f:
#         instructions.append(0)

#         line = line.split()

#         if line[0] == "addx":
#             instructions.append(int(line[1]))

# # Part A
# total = 0
# val = 1

# checks = set([20, 60, 100, 140, 180, 220])

# for step, add_value in enumerate(instructions):
#     if step + 1 in checks:
#         total += (step + 1) * val

#     val += add_value

# print(total)

# # Part B
# val = 1

# for step, add_value in enumerate(instructions):
#     row_pos = step % 40

#     if row_pos == 0:
#         print()

#     if row_pos in [val - 1, val, val + 1]:
#         print("#", end="")
#     else:
#         print(".", end="")

#     val += add_value

from pathlib import Path

path = (Path(__file__).parent / "./q10.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        data.append(0)

        line = line.strip().split()
        if len(line) > 1:
            data.append(int(line[1]))

# Part A
total = 0
checks = set([20, 60, 100, 140, 180, 220])

x = 1

for i, val in enumerate(data):
    if (i + 1) in checks:
        total += (i + 1) * x
    
    x += val

print(total)

# Part B
x = 1

for i, val in enumerate(data):
    row_pos = i % 40

    if row_pos == 0:
        print()

    if row_pos in [x - 1, x, x + 1]:
        print("#", end="")
    else:
        print(".", end="")

    x += val