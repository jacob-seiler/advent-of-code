order = """
2x3x4
"""

total = 0
ribbons = 0

for box in order.split("\n"):
    dims = box.strip().split("x")
    
    if len(dims) != 3:
        continue

    l = int(dims[0])
    w = int(dims[1])
    h = int(dims[2])

    side_1 = l * w
    side_2 = w * h
    side_3 = h * l

    sa = 2 * side_1 + 2 * side_2 + 2 * side_3
    total += sa + min(side_1, side_2, side_3)

    smallest = min(l, w, h)
    largest = max(l, w, h)
    middlest = l + w + h  - smallest - largest

    ribbons += 2 * smallest + 2 * middlest
    ribbons += l * w * h

print(total, ribbons)
