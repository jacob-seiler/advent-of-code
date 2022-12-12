from pathlib import Path

path = (Path(__file__).parent / "./q5.txt").resolve()

overlaps = set()
points = set()

def savePoints(x, y):
    if (x, y) in points:
        overlaps.add((x, y))

    points.add((x, y))

def savePath(x1, y1, x2, y2):
    pos_x, pos_y = x1, y1

    while pos_x != x2 or pos_y != y2:
        savePoints(pos_x, pos_y)

        dist_x = abs(x2 - x1)
        dist_y = abs(y2 - y1)

        pos_x += 0 if dist_x == 0 else (x2 - x1) // dist_x
        pos_y += 0 if dist_y == 0 else (y2 - y1) // dist_y

    savePoints(pos_x, pos_y)

with open(path) as f:
    for line in f:
        line = line.strip()
        coords1, coords2 = line.split(" -> ")

        x1, y1 = coords1.split(',')
        x2, y2 = coords2.split(',')
        
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        # Uncomment for part 1
        # if x1 != x2 and y1 != y2:
        #     continue
        
        savePath(x1, y1, x2, y2)

print(len(overlaps))
