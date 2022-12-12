from pathlib import Path

path = (Path(__file__).parent / "./q12.txt").resolve()
data = []

def convert_to_num(char):
    if char == 'S':
        return -1

    if char == 'E':
        return 1000

    return ord(char) - ord('a')

with open(path) as f:
    for line in f:
        line = line.strip()
        line = [convert_to_num(c) for c in line]
        data.append(line)

pos = None
goal = None

for row in range(len(data)):
    for col in range(len(data[row])):
        val = data[row][col]

        if val == -1:
            pos = [row, col]

        if val == 1000:
            goal = [row, col]

        if pos != None and goal != None:
            break

dp = dict()
best_goal = None

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def find_goal(grid, pos, visited=None):
    global best_goal, dp

    if visited == None:
        visited = set([pos])

    if best_goal != None and len(visited) >= best_goal:
        return None

    if pos in dp:
        if dp[pos] <= len(visited):
            return None

    dp[pos] = len(visited)
    steps = None

    for dir_row, dir_col in DIRS:
        if pos[0] + dir_row == -1 or pos[0] + dir_row == len(grid):
            continue

        if pos[1] + dir_col == -1 or pos[1] + dir_col == len(grid[pos[0]]):
            continue

        move = (pos[0] + dir_row, pos[1] + dir_col)
        move_val = grid[move[0]][move[1]]
        val = grid[pos[0]][pos[1]]

        if move in visited:
            continue

        if val != -1 and not (val == 25 and move_val == 1000) and move_val - val >= 2:
            continue

        if move_val == 1000:
            if best_goal == None or len(visited) < best_goal:
                best_goal = len(visited)
            
            return len(visited)
        
        visited_copy = visited.copy()
        visited_copy.add(move)

        steps_local = find_goal(grid, move, visited_copy)

        if steps_local != None and (steps == None or steps > steps_local):
            steps = steps_local

    return steps

possibilities = []

for row in range(len(data)):
    for col in range(len(data[row])):
        if data[row][col] in [0, -1]:
            possibilities.append((row, col))

best = None

for i, p in enumerate(possibilities):
    print("Iteration", i + 1, "/", len(possibilities))
    steps = find_goal(data, p)

    if steps == None:
        continue

    if best == None or steps < best:
        best = steps

print(best)