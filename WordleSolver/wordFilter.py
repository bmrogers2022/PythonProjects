# getting words
with open('WordleSolver\everyFiveLetterWord.txt') as everyPossible:
    words = everyPossible.read().splitlines()

'''
everything below this line was made a long time ago, there are 
a lot of optimizations to be made (namely in computersfavorite(),
due to the poor handling of lists and horribly inefficient tempCriteria function),
but this is one of the first things I ever made and I don't want to damage its history
by changing anything. The median solve time when I used this program to do the wordle was 3 guesses.
'''

# recommended first guess by program = tares

# put greens as ('letter', index)
greens = []
# put grays as strings
grays = []
# put yellows in as ('letter', failedIndex)
yellows = []

# user friendly :)
grayInput = input('every gray letter, no spaces: ')
for letter in grayInput:
    grays.append(letter)
yellowInput = input('every yellow letter with index, followed by a space for a new input: ')
try:
    for pair in yellowInput.split(' '):
        yellows.append((pair[0], int(pair[1])))
except:
    pass
greenInput = input('every green letter with index, followed by a space for a new input: ')
try:
    for pair in greenInput.split(' '):
        greens.append((pair[0], int(pair[1])))
except:
    pass

# checking for first guess
if grays == [] and yellows == [] and yellows == []:
    FirstGuess = True
else:
    FirstGuess = False

# word for computer's favorite
bestGuess = ('', float('inf'))

# filter function to check each word against current parameters
def criteria(words):
    for gray in grays:
        if gray in words:
            return False
    for yellow in yellows:
        if yellow[0] not in words or yellow[0] == words[yellow[1]]:
            return False
    for green in greens:
        if green[0] != words[green[1]]:
            return False
    return True

# filter function to avoid guessing a word with double letters
def idealGuesses(words):
    used = []
    for letter in words:
        if letter in used:
            return False
        else:
            used.append(letter)
    return True

# filter function to find the word that has the best chance of being a good guess (not working)
def computersFavorite():
    global bestGuess
    # there's gotta be some other way to do this :/ (I can't add parameters because of filter())
    def tempCriteria(words):
        for gray in tempGray:
            if gray in words:
                return False
        for yellow in tempYellow:
            if yellow[0] not in words or yellow[0] == words[yellow[1]]:
                return False
        for green in tempGreen:
            if green[0] != words[green[1]]:
                return False
        return True
    # get words returns all possible words
    if FirstGuess:
        first = list(filter(firstGuess, ideals))
        print(f'length of firsts = {len(first)}')
        for word in first:
            totalPossibles = 0
            # checking which guess removes most possibilities through simulating every possibility
            for possible in ideals:
                # setting new lists equal to the original list
                tempGreen = []
                for line in greens:
                    tempGreen.append(line)
                tempYellow = []
                for line in yellows:
                    tempYellow.append(line)
                tempGray = []
                for line in grays:
                    tempGray.append(line)
                for letter in word:
                    if letter not in possible:
                        tempGray.append(letter)
                    elif letter in possible and word.index(letter) != possible.index(letter):
                        tempYellow.append((letter, word.index(letter)))
                    elif letter in possible and word.index(letter) == possible.index(letter):
                        tempGreen.append((letter, word.index(letter)))
                hypotheticalPossibles = list(filter(tempCriteria, possibles))
                totalPossibles += len(hypotheticalPossibles)
            if totalPossibles < bestGuess[1]:
                bestGuess = (word, totalPossibles)
                with open('bestGuesses.txt', 'a') as trackingFile:
                    trackingFile.write(f'current best (final with EVERY guess) = {bestGuess}\n')
    else: 
        for word in ideals:
            totalPossibles = 0
            # checking which guess removes most possibilities through simulating every possibility
            for possible in possibles:
                # setting lists equal to the original list had a weird property of making original lists inherit things appended to the new lists
                tempGreen = []
                for line in greens:
                    tempGreen.append(line)
                tempYellow = []
                for line in yellows:
                    tempYellow.append(line)
                tempGray = []
                for line in grays:
                    tempGray.append(line)
                for letter in word:
                    if letter not in possible:
                        tempGray.append(letter)
                    elif letter in possible and word.index(letter) != possible.index(letter):
                        tempYellow.append((letter, word.index(letter)))
                    elif letter in possible and word.index(letter) == possible.index(letter):
                        tempGreen.append((letter, word.index(letter)))
                hypotheticalPossibles = list(filter(tempCriteria, possibles))
                totalPossibles += len(hypotheticalPossibles)
            if totalPossibles < bestGuess[1]:
                bestGuess = (word, totalPossibles)
                with open('bestGuesses.txt', 'a') as trackingFile:
                    trackingFile.write(f'current best = {bestGuess}\n')
    print(f'rec guess: {bestGuess}')

# filter command for finding ideal first guess
def firstGuess(ideals):
    for letter in 'eta':
        if letter not in ideals:
            return False
    for letter in 'qwyuipozxvbmnkjhd':
        if letter in ideals:
            return False
    return True

# executing all filters and displaying possible guesses
def getWords():
    global possibles
    global ideals
    possibles = list(filter(criteria, words))
    print(f'possibles = {possibles}')
    ideals = list(filter(idealGuesses, possibles))
    print(f'ideals = {ideals}')

getWords()
# computerFavorite() is optional, intuition is nearly equally as accurate, but it was really hard to make so I use it even though it's slow
computersFavorite()
