lines = open('q7.txt').read().strip().split("\n")
scores = {hand:int(score) for (hand, score) in [line.split() for line in lines]}

def calc_hand_type(hand, part2):
    occurences = {card:hand.count(card) for card in hand}

    if part2:
        if len(occurences) > 1 and 'J' in occurences:
            most_common_card = max([card for card in occurences if card != 'J'], key=occurences.get)
            occurences[most_common_card] += occurences['J']
            del occurences['J']

    # 5 of a kind
    if len(occurences) == 1:
        return 'a'
    
    if len(occurences) == 2:
        # 4 of a kind
        if 4 in occurences.values():
            return 'b'
        
        # Full house
        return 'c'
    
    if len(occurences) == 3:
        # 3 of a kind
        if 3 in occurences.values():
            return 'd'
        
        # 2 pairs
        return 'e'
    
    if len(occurences) == 4:
        # 1 pair
        return 'f'
    
    # High card
    return 'g'

def calc_ranking(hand, part2):
    value = [calc_hand_type(hand, part2)]

    values = {
        'A': 'a',
        'K': 'b',
        'Q': 'c',
        'J': 'n' if part2 else 'd',
        'T': 'e',
        '9': 'f',
        '8': 'g',
        '7': 'h',
        '6': 'i',
        '5': 'j',
        '4': 'k',
        '3': 'l',
        '2': 'm'
    }

    for card in hand:
        value.append(values[card])

    return ''.join(value)

for part2 in [False, True]:
    hands = sorted([line.split()[0] for line in lines], key=lambda x : calc_ranking(x, part2))
    total = 0

    for rank, card in enumerate(hands[::-1]):
        total += scores[card] * (rank + 1)

    print(total)
