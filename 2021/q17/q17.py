from pathlib import Path

path = (Path(__file__).parent / "./q17.txt").resolve()

target_x = []
target_y = []

with open(path) as f:
    for line in f:
        data = line.strip()
        x, y = data.split(", ")
        
        target_x = [int(i) for i in x[15:].split("..")]
        target_y = [int(i) for i in y[2:].split("..")]

# print(target_x, target_y)

"""
"""

# temp = [(27, -5), (28, -6), (30, -9), (8, 0), (11, -4), (25, -5), (15, -4), (29, -5), (20, -8), (21, -9), (6, 2), (7, 1), (12, -3), (30, -7), (11, -2), (11, -1), (15, -2), (21, -7), (23, -10), (6, 4), (7, 3), (27, -10), (30, -5), (25, -10), (24, -6), (26, -9), (29, -10), (21, -5), (23, -8), (6, 6), (7, 5), (27, -8), (28, -9), (13, -4), (26, -7), (29, -8), (7, 7), (27, -6), (28, -7), (30, -10), (9, -1), (13, -2), (26, -5), (21, -10), (6, 1), (7, 0), (7, 9), (20, -6), (22, -9), (14, -4), (28, -5), (30, -8), (9, 0), (11, -3), (24, -9), (15, -3), (7, 2), (22, -7), (14, -2), (24, -7), (26, -10), (25, -8), (7, 4), (22, -5), (23, -6), (6, 8), (28, -10), (24, -5), (26, -8), (25, -6), (29, -6), (20, -9), (12, -4), (28, -8), (8, 1), (10, -1), (13, -3), (26, -6), (20, -7), (22, -10), (21, -8), (6, 3), (12, -2), (30, -6), (24, -10), (20, -5), (22, -8), (21, -6), (23, -9), (6, 5), (14, -3), (27, -9), (24, -8), (25, -9), (29, -9), (22, -6), (23, -7), (6, 7), (7, 6), (27, -7), (8, -1), (25, -7), (29, -7), (20, -10), (23, -5), (6, 9), (7, 8)]
# temp = set(temp)

# temp2 = "23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5     25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7     8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6     26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3     20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8     25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7     25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6     8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4     24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5     7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3     23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5     27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5     8,-2    27,-8   30,-5   24,-7"
# temp2 = temp2.split()
# temp2 = [(int(j), int(k)) for j, k in (i.split(",") for i in temp2)]
# temp2 = set(temp2)

# for p in temp2:
#     if p not in temp:
#         print(p)

"""
"""

# Part A
def in_target(x, y, target_x, target_y):
    return x >= target_x[0] and x <= target_x[1] and y >= target_y[0] and y <= target_y[1]

largest = None

for attemp in range(1000):
    success = False
    
    x, y = target_x[0] + 1, 0
    vel_x, vel_y = 0, attemp

    while y >= target_y[0]:
        x += vel_x
        y += vel_y

        vel_y -= 1

        if in_target(x, y, target_x, target_y):
            success = True
            break

    if not success:
        continue

    if largest == None:
        largest = attemp
    else:
        largest = max(largest, attemp)

y_max = largest * (largest + 1) // 2
print(largest, y_max)

# Part B
RANGE = 400
total = 0
vels = set()

for attemp_x in range(-1 * RANGE, RANGE):
    # print(str(((attemp_x + RANGE) / (RANGE * 2)) * 100) + "%")

    for attemp_y in range(-1 * RANGE, RANGE):
        success = False
        
        x, y = 0, 0
        vel_x, vel_y = attemp_x, attemp_y

        while y >= target_y[0]:
            x += vel_x
            y += vel_y

            vel_y -= 1

            if vel_x != 0:
                if vel_x > 0:
                    vel_x -= 1
                else:
                    vel_x += 1

            if in_target(x, y, target_x, target_y):
                success = True
                break

        if success:
            total += 1
            vels.add(tuple([attemp_x, attemp_y]))

print(total)