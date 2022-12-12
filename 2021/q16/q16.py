from pathlib import Path

path = (Path(__file__).parent / "./q16.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        data = line.strip()

temp = len(data)
data = format(int(data, 16), "0b")

while len(data) < temp * 4:
    data = "0" + data

def parse_packet(data, index=0):
    total = 0
    
    total += int(data[index:index + 3], 2)
    type_id = int(data[index + 3:index + 6], 2)

    index += 6
    value = ""

    if type_id == 4:
        while data[index] != "0":
            value += data[index + 1: index + 5]
            index += 5
        
        value += data[index + 1: index + 5]
        value = int(value, 2)
        index += 5

        return total, index, value

    if value == "":
        value = None
        
    length_type = int(data[index], 2)
    length_amount = 15 if length_type == 0 else 11

    index += 1
    length = int(data[index:index + length_amount], 2)
    index += length_amount

    bits_starting = index
    packets_parsed = 0

    while (length_type == 0 and (index - bits_starting) < length) or (length_type == 1 and packets_parsed < length):
        t, i, v = parse_packet(data, index)
        index = i
        packets_parsed += 1
        total += t
        
        if value == None:
            value = v
            continue

        # sum
        if type_id == 0:
            value += v
            continue
        
        # product
        if type_id == 1:
            value *= v
            continue
        
        # minimum 
        if type_id == 2:
            value = min(value, v)
            continue
        
        # maximum 
        if type_id == 3:
            value = max(value, v)
            continue

        value -= v
        
    # greater than
    if type_id == 5:
        value = 1 if value > 0 else 0
    
    # less than
    if type_id == 6:
        value = 1 if value < 0 else 0
    
    # equal to
    if type_id == 7:
        value = 1 if value == 0 else 0

    return total, index, value

total, i, value = parse_packet(data)
print("Part A", total)
print("Part B", value)