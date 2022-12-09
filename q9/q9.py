from pathlib import Path

path = (Path(__file__).parent / "./q9.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        data.append(line)

visited = set([(0, 0)])
visited_butt = set([(0, 0)])

head = [0, 0]
tails = [[0, 0] for _ in range(9)]

def move_tail(head, tail):
    diff_x = head[0] - tail[0]
    diff_y = head[1] - tail[1]

    dir_x = -1 if tail[0] < head[0] else 1
    dir_y = -1 if tail[1] < head[1] else 1

    # Diagonal
    if abs(diff_x) >= 2 and abs(diff_y) >= 2:
        tail[0] = head[0] + dir_x
        tail[1] = head[1] + dir_y

    # Sideways
    elif abs(diff_x) >= 2:
        tail[0] = head[0] + dir_x
        tail[1] = head[1]

    # Up / down
    elif abs(diff_y) >= 2:
        tail[0] = head[0]
        tail[1] = head[1] + dir_y

DIRS_X = {"U": 0, "D": 0, "L": -1, "R": 1}
DIRS_Y = {"U": -1, "D": 1, "L": 0, "R": 0}

for line in data:
    dir, amount = line.split(" ")
    amount = int(amount)

    for _ in range(amount):
        diff_x = DIRS_X[dir]
        diff_y = DIRS_Y[dir]

        # Move head
        head[0] += diff_x
        head[1] += diff_y

        # Move tails
        for i, tail in enumerate(tails):
            temp = head if i == 0 else tails[i - 1]
            move_tail(temp, tail)

        visited.add(tuple(tails[0]))
        visited_butt.add(tuple(tails[-1]))

print(len(visited))
print(len(visited_butt))
