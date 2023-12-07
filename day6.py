# Problem: https://adventofcode.com/2023/day/6

# Part One
race_times = [45, 97, 72, 95]
race_distances = [305, 1062, 1110, 1695]

def findInterval(race):
    '''
    Finds how many different ways you can beat the high score in race_distances
    "Beating the score" is determined by multiplying the speed of the boat by how much time left the boat can go
    Speed of the boat is determined by how long one holds the boat before it goes
    '''
    time = race_times[race]
    distance = race_distances[race]
    faster_times = []
    for n in range(time):
        curr_distance = n * (time - n)
        if curr_distance > distance:
            faster_times.append(n)

    return len(faster_times)

# Gets the number of ways you can beat the high scores by multiplying them together
answer = 1
for index in range(4):
    answer *= findInterval(index)

print(f"Part One: {answer}")


# Part two
race_times = [45977295]
race_distances = [305106211101695]

print(f"Part Two: {findInterval(0)}")
