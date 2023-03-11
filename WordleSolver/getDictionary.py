with open('everyWord.txt') as everyWord:
    words = everyWord.readlines()

def checkFive(words):
    # reason it is six instead of five is new line character
    if len(words) == 6:
        return True
    return False

updatedWords = filter(checkFive, words)

# how I made the everyFiveLetterWord file
with open('everyFiveLetterWord.txt', 'w') as newFile:
    for word in updatedWords:
        newFile.write(word)
