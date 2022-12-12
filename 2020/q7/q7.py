from pathlib import Path

path = (Path(__file__).parent / "./q7.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        bag, rules = line.strip().split(" contain ")
        bag = bag[:-5]
        rules = rules[:-1].split(", ")

        for i in range(len(rules)):
            val = rules[i].split()[0]
            if val == "no":
                val = 0

            val = int(val)

            rules[i] = val, ' '.join(rules[i].split()[1:])[:-4].strip()

        if rules[0][1] == "other":
            rules = []
        
        print(bag, rules)

        data.append((bag, rules))

colors = set()
something_added = True

while something_added:
    something_added = False

    for bag, rules in data:
        for val, rule in rules:
            if val > 0 and (rule == "shiny gold" or rule in colors):
                if bag not in colors:
                    colors.add(bag)
                    something_added = True
                
                break

struc = dict()

for bag, rules in data:
    struc[bag] = rules

def calc_total(bag):
    total = 0

    for val, rule in struc[bag]:
        total += val
        total += val * calc_total(rule)

    return total

required = calc_total("shiny gold")

print(len(colors))
print(required)
