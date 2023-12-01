# Read q1.txt into lines list and strip and clean each line
lines = []

with open('q1.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())

total = 0
words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"}

for line in lines:
    digits = []

    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(line[i])
            continue

        # Part 2
        for word in words:
            if line[i:].startswith(word):
                digits.append(words[word])
                break

    total += int(digits[0] + digits[-1])

print(total)
