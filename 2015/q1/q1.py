floors = "()()(((())()(()))))))))((()(((((((((())))"

pos = 0

for index, floor in enumerate(floors):
    if floor == "(":
        pos += 1
    else:
        pos -= 1

    # Part 2
    if pos == -1:
        print(index + 1)
        break

# Part 1
# print(pos)