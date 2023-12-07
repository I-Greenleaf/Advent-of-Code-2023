# Problem: https://adventofcode.com/2023/day/6

# Part One
race_times = [45, 97, 72, 95]
race_distances = [305, 1062, 1110, 1695]

def findInterval(race):
    time = race_times[race]
    distance = race_distances[race]
    faster_times = []
    for n in range(time):
        curr_distance = n * (time - n)
        if curr_distance > distance:
            faster_times.append(n)

    return len(faster_times)

answer = 1
for index in range(4):
    answer *= findInterval(index)

print(f"Part One: {answer}")


# Part two
race_times = [45977295]
race_distances = [305106211101695]

print(f"Part Two: {findInterval(0)}")
