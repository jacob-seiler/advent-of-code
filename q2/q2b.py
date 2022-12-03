from pathlib import Path

path = (Path(__file__).parent / "./q2.txt").resolve()

VALUE_ROCK = "A"
VALUE_PAPER = "B"
VALUE_SCISSORS = "C"

logic = {
    VALUE_ROCK: {"points": 1, "beats": VALUE_SCISSORS, "draws": VALUE_ROCK, "loses": VALUE_PAPER}, # rock
    VALUE_PAPER: {"points": 2, "beats": VALUE_ROCK, "draws": VALUE_PAPER, "loses": VALUE_SCISSORS}, # paper
    VALUE_SCISSORS: {"points": 3, "beats": VALUE_PAPER, "draws": VALUE_SCISSORS, "loses": VALUE_ROCK} # scissors
    }

SCORE_LOSE = 0
SCORE_DRAW = 3
SCORE_WIN = 6

total = 0

with open(path) as f:
    for line in f:
        elf, you = line.strip().split(' ')

        if you == "X":
            # lose
            pick = logic[elf]["beats"]
            total += SCORE_LOSE + logic[pick]["points"]
        elif you == "Y":
            # draw
            pick = logic[elf]["draws"]
            total += SCORE_DRAW + logic[pick]["points"]
        else:
            # win
            pick = logic[elf]["loses"]
            total += SCORE_WIN + logic[pick]["points"]

print(total)