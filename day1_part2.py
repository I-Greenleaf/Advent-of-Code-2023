# Problem: https://adventofcode.com/2023/day/1

import re

# Gets the data and puts each calibration as a string in a list
with open('day1.txt', 'r') as file:
    calibrations = file.readlines()

# Used to convert numbers in text form to numerical form
text_to_num = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
    'oneight':'18',
    'twone':'21',
    'eightwo': '82'
}

# Takes each number (whether text or numerical) and puts in into a list
# Then takes the first and last number that appears in each calibration
all_digits = []
first_last_digits = []
for index, calibration in enumerate(calibrations):
    all_digits.append(re.findall('1|2|3|4|5|6|7|8|9|0|oneight|twone|eightwo|one|two|three|four|five|six|seven|eight|nine', calibration))
    first_last_digits.append([all_digits[index][0], all_digits[index][-1]])

# Goes through each number and converts text numbers to numberical form using the text_to_num dictionary 
for indexA, pair in enumerate(first_last_digits):
    for indexB, digit in enumerate(pair):
        if len(digit) > 1:
            first_last_digits[indexA][indexB] = text_to_num[digit]
            if len(first_last_digits[indexA][indexB]) == 2:
                '''
                Checks for the numbers where the last and first letter of the numbers are shared
                Splits the numbers into their individual numbers 
                Then deletes the number that is inbetween the starting and ending number in the calibration
                '''
                first_last_digits[indexA].insert(indexB+1, first_last_digits[indexA][indexB][1])
                first_last_digits[indexA][indexB] = first_last_digits[indexA][indexB][0]
                first_last_digits[indexA].pop(1)
    first_last_digits[indexA] = first_last_digits[indexA][0] + first_last_digits[indexA][1]

# Finds the sum of all calibration numbers
sum = 0
for num in first_last_digits:
    sum += int(num)
print(sum)
