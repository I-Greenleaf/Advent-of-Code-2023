# Problem: https://adventofcode.com/2023/day/7


hands = []

# Takes a file of the given vaules and converts it into the list hands
# where each element in the list is another list that contains the string of cards and the bid of the hand as a string
with open('day7.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        hands.append(line.split())


def handType(hand):
    '''
    Takes a hand/string of cards and then returns a int that refers to what type of hand it is, for the Camel Cards game
    The higher the returned int, the better the hand is compared to the ones below it
    The function does so by putting the number of time a card appears into a dictionary
        (e.g. "29K22" is {'2':3, '9':1, 'K':1})
    Then it puts those numbers in a new dictionary to see how many of a kind appears in a hand
        (e.g. {'2':3, '9':1, 'K':1} is {1:2, 3:1})
    It then sees what type of hand the hand is based on this array
        (e.g. {1:2, 3:1} is a Three of a kind and not a Full House because two different cards appeared and not a pair)

    However, this function is different than Part 1's as seperately counts the Jack cards as they are seen as wild cards
    '''
    numOfCardsDict = {}
    j_counter = 0
    for card in hand:
        if card == 'J':
            j_counter += 1
        elif card in numOfCardsDict:    
            numOfCardsDict[card] += 1
        else:
            numOfCardsDict[card] = 1

    # Takes the Jacks and counts them as the card that appears the most
    if j_counter == 5:          # Checks for case where numOfCardsDict has no keys and values because all 5 cards are Jacks
        numOfCardsDict['J'] = 5
    elif j_counter > 0:
        for j in range(j_counter):
            mostFrequentCard = max(numOfCardsDict, key=numOfCardsDict.get)
            numOfCardsDict[mostFrequentCard] += 1

    numOfCards = sorted(numOfCardsDict.values(), reverse=True)
    
    numofNumsDict = {}
    for num in numOfCards:
        if num in numofNumsDict:    
            numofNumsDict[num] += 1
        else:
            numofNumsDict[num] = 1

    # Checks for what type of hand the hand is
    if 5 in numofNumsDict:          # Checks for a Five of a kind
        return 6
    elif 4 in numofNumsDict:        # Checks for a Four of a kind
        return 5
    elif 3 in numofNumsDict: 
        if 2 in numofNumsDict:      # Checks for a Full house
            return 4
        else:                       # Checks for a Three of a kind
            return 3
    elif 2 in numofNumsDict:
        if numofNumsDict[2] == 2:   # Checks for a Two pair
            return 2
        else:                       # Checks for a One pair
            return 1
    else:                           # Checks for a High Card
        return 0

'''
Finds the strength of each hand by assigning a hand an value with an abitrary scale (Same scale is applied to each hand making them compareable)
First it finds the type of hand
Then it assigns numbers following that first number based
Does going through the ordered hand and assigning each card a hexdecimal value
    Hexdecimal values are used so that each value can be a single digit
Converts hex number to an integer value and adds it to each hand's list
'''
for hand in hands:
    cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']   # Difference from Part 1: 
    strength = str(handType(hand[0]))
    for card in hand[0]:
        strength += str(hex(cards.index(card) + 2))[2::]
    
    hand.append(int(strength, 16))

# Sorts all the hands based on its strength
hands.sort(key=lambda x: x[2])

# Adds the sum of the "rank" * the strength of hand, for all hands
# Rank system has the worst hand as 1 and the best as len(hands)-1
sum = 0
for index, hand in enumerate(hands, start=1):
    sum += index * int(hand[1])
print(sum)
