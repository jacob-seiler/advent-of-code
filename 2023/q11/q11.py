lines = [list(x) for x in open('q11.txt').read().strip().split('\n')]
empty_rows = set([i for i, x in enumerate(lines) if all(y == '.' for y in x)])
empty_columns = set([i for i in range(len(lines[0])) if all(x[i] == '.' for x in lines)])

# def expand(lines):
#     empty_rows = set([i for i, x in enumerate(lines) if all(y == '.' for y in x)])
#     empty_columns = set([i for i in range(len(lines[0])) if all(x[i] == '.' for x in lines)])

#     new_lines = [x[:] for x in lines]

#     for row in range(len(lines) - 1, -1, -1):
#         if row in empty_rows:
#             new_lines.insert(row + 1, ['.'] * len(lines[0]))

#     for column in range(len(lines[0]) - 1, -1, -1):
#         if column in empty_columns:
#             for row in range(len(new_lines)):
#                 new_lines[row].insert(column + 1, '.')

#     return new_lines

star_positions = []

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == '#':
            star_positions.append((x, y))

def distance(x1, y1, x2, y2):
    expansion = 1000000 - 1 # for part 1 make this value 1
    dist = abs(x2 - x1) + abs(y2 - y1)

    # check if x1 to x2 passes through any columns in empty_columns
    for column in empty_columns:
        if x1 < column < x2 or x2 < column < x1:
            dist += expansion

    # same thing but for rows
    for row in empty_rows:
        if y1 < row < y2 or y2 < row < y1:
            dist += expansion

    return dist

total = 0

for i, star in enumerate(star_positions):
    for j, compare in enumerate(star_positions[i + 1:]):
        dist = distance(*star, *compare)
        total += dist

print(total)