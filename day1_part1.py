# Problem: https://adventofcode.com/2023/day/1

# Gets the data and puts each calibration as a string in a list
with open('day1.txt', 'r') as file:
    calibrations = file.readlines()

# Takes the first and last number in a calibration and combinds the digits into a two digit number
# Puts this number into a list
numbers = []
for calibration in calibrations:
    number = ''
    indexA = 0
    # Checks for the first number in a calibration
    for indexA, char in enumerate(calibration):
        if char.isdigit():
            number += char
            break
    # Checks for the last number in a calibration by checking for the first number in the reversed calibration
    for indexB, char in enumerate(calibration[::-1]):
        if char.isdigit():
            number += char
            break
    if len(number) > 0:
        numbers.append(number)

# Finds the sum of all calibration numbers
sum = 0
for num in numbers:
    sum += int(num)
print(sum)
