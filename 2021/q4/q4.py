from pathlib import Path

path = (Path(__file__).parent / "./q4.txt").resolve()

data = []

with open(path) as f:
    for line in f:
        data.append(line.strip())

draws = [int(i) for i in data[0].split(',')]
boards = []

def cleanRow(row):
    cleaned = []
    row = row.split(' ')

    for num in row:
        if num == "":
            continue

        cleaned.append(int(num))

    return cleaned

for i in range(2, len(data), 6):
    board = [
        cleanRow(data[i]),
        cleanRow(data[i + 1]),
        cleanRow(data[i + 2]),
        cleanRow(data[i + 3]),
        cleanRow(data[i + 4])
    ]

    boards.append(board)

def checkWin(board, draws):
    # Check rows
    for row in board:
        if len(set(row).intersection(draws)) == 5:
            return True

    for col in range(5):
        vals = set()
        vals.add(board[0][col])
        vals.add(board[1][col])
        vals.add(board[2][col])
        vals.add(board[3][col])
        vals.add(board[4][col])

        if len(draws.intersection(vals)) == 5:
            return True

    return False

def findWinners():
    skips = set()
    winners = []
    drawn = set()

    for draw in draws:
        drawn.add(draw)

        for i, board in enumerate(boards):
            if i in skips:
                continue
            
            if checkWin(board, drawn):
                winners.append(calcScore(boards[i], drawn, draw))
                skips.add(i)

    return winners

def calcScore(board, drawn, just_called):
    total = 0

    for row in board:
        for num in row:
            if num not in drawn:
                total += num

    return just_called * total

winners = findWinners()
print("Part 1", winners[0])
print("Part 2", winners[-1])