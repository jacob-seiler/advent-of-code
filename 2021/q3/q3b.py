from pathlib import Path

path = (Path(__file__).parent / "./q3.txt").resolve()

data = []

with open(path) as f:
    for line in f:
        data.append(line.strip())

def find_oxygen_gen_rating(data, index=0):
    if index >= 12:
        return None

    diff = 0
    ones = []
    zeros = []

    for bits in data:
        if bits[index] == "1":
            ones.append(bits)
            diff += 1
            continue

        zeros.append(bits)
        diff -= 1

    keep = ones if diff >= 0 else zeros

    if len(keep) == 1:
        return int(keep[0], 2)

    return find_oxygen_gen_rating(keep, index + 1)

def find_co2_scrubber_rating(data, index=0):
    if index >= 12:
        return None

    diff = 0
    ones = []
    zeros = []

    for bits in data:
        if bits[index] == "1":
            ones.append(bits)
            diff += 1
            continue

        zeros.append(bits)
        diff -= 1

    keep = zeros if diff >= 0 else ones

    if len(keep) == 1:
        return int(keep[0], 2)

    return find_co2_scrubber_rating(keep, index + 1)

ogr = find_oxygen_gen_rating(data)
csr = find_co2_scrubber_rating(data)

print(ogr * csr)