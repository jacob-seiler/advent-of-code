from pathlib import Path

path = (Path(__file__).parent / "./q2.txt").resolve()

VALUE_ROCK = "A"
VALUE_PAPER = "B"
VALUE_SCISSORS = "C"

logic = {
    "X": {"points": 1, "beats": VALUE_SCISSORS, "draws": VALUE_ROCK}, # rock
    "Y": {"points": 2, "beats": VALUE_ROCK, "draws": VALUE_PAPER}, # paper
    "Z": {"points": 3, "beats": VALUE_PAPER, "draws": VALUE_SCISSORS} # scissors
    }

SCORE_LOSE = 0
SCORE_DRAW = 3
SCORE_WIN = 6

total = 0

with open(path) as f:
    for line in f:
        elf, you = line.strip().split(' ')
        total += logic[you]["points"]

        if logic[you]["beats"] == elf:
            total += SCORE_WIN
        elif logic[you]["draws"] == elf:
            total += SCORE_DRAW
        else:
            total += SCORE_LOSE

print(total)