lines = open('q6.txt').read().strip().split("\n")
times = [int(x) for x in lines[0].split(':')[1].split()]
distances = [int(x) for x in lines[1].split(':')[1].split()]

# Part 2 (takes a while to run).
# Comment out the 2 lines below for part 1's solution.
times = [int(''.join(str(x) for x in times))]
distances = [int(''.join(str(x) for x in distances))]

races = [(times[i], distances[i]) for i in range(len(times))]

total = 0

for time, distance in races:
    options = 0

    for speed in range(1, time):
        remaining_time = time - speed
        end_distance = speed * remaining_time

        if end_distance > distance:
            options += 1

    if options > 0:
        if total == 0:
            total = options
        else:
            total *= options

print(total)
