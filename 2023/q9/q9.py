lines = open('q9.txt').read().strip().split("\n")
lines = [[int(x) for x in line.split()] for line in lines]

total = 0
total_2 = 0

for line in lines:
    diffs = [line[::]]

    while len(set(diffs[-1])) != 1:
        diff = diffs[-1]
        new_diff = []

        for i in range(1, len(diff)):
            val = diff[i] - diff[i - 1]
            new_diff.append(val)

        diffs.append(new_diff)
    
    diffs[-1].append(diffs[-1][0])
    diffs[-1].append(diffs[-1][0]) # part 2
    prev_diff = diffs[-1]

    for i in range(len(diffs) - 2, -1, -1):
        new_val = diffs[i][-1] + prev_diff[-1]
        diffs[i].append(new_val)

        # part_2
        new_val = diffs[i][0] - prev_diff[0]
        diffs[i].insert(0, new_val)
        
        prev_diff = diffs[i]

    total += diffs[0][-1]
    total_2 += diffs[0][0] # part 2

    print(diffs)

print(total)
print(total_2)