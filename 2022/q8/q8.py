from pathlib import Path

path = (Path(__file__).parent / "./q8.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        data.append([int(i) for i in line])

visible = 0
score = 0

def is_visible(data, row, col):
    if row == 0 or row == len(data) - 1:
        return True, 0

    if col == 0 or col == len(data[row]) - 1:
        return True, 0

    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    tree = data[row][col]
    
    is_seen = False
    can_see = 1

    for dir in DIRS:
        tallest = True
        can_see_dir = 1

        pos_row = row
        pos_col = col

        while True:
            pos_row += dir[0]
            pos_col += dir[1]

            if pos_row < 0 or pos_row >= len(data):
                can_see_dir -= 1
                break

            if pos_col < 0 or pos_col >= len(data[row]):
                can_see_dir -= 1
                break

            pos = data[pos_row][pos_col]

            if pos >= tree:
                tallest = False
                break

            can_see_dir += 1

        can_see *= can_see_dir

        if tallest:
            is_seen = True
    
    return is_seen, can_see

for row in range(len(data)):
    for col in range(len(data[row])):
        is_seen, can_see = is_visible(data, row, col)

        score = max(score, can_see)

        if is_seen:
            visible += 1

print(visible)
print(score)
