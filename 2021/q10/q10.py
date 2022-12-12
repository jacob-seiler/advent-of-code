from pathlib import Path

path = (Path(__file__).parent / "./q10.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        data.append(line)

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

correct_score = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

errors = []
correct_scores = []

def calc_score(stack):
    score = 0

    while len(stack) > 0:
        score *= 5
        score += correct_score[stack.pop()]

    return score

# Part A
for line in data:
    stack = []
    perfect = True

    for char in line:
        if char in pairs:
            stack.append(char)
            continue
        
        val = pairs[stack.pop()]
        if val != char:
            errors.append(char)
            perfect = False
            break

    # Part B
    if perfect:
        correct_scores.append(calc_score(stack))

total = 0

for error in errors:
    total += score[error]

print(total)
print(sorted(correct_scores)[len(correct_scores) // 2])