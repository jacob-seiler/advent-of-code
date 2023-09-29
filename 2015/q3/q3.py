dirs = "^>v<"

positions = {(0, 0)}
curr = (0, 0)
robo = (0, 0)

actions = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}

for dir in dirs[::2]:
    action = actions[dir]
    curr = (curr[0] + action[0], curr[1] + action[1])

    positions.add(curr)

for dir in dirs[1::2]:
    action = actions[dir]
    robo = (robo[0] + action[0], robo[1] + action[1])

    positions.add(robo)

print(len(positions))
