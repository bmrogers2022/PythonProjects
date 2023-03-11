# I did this because I thought it would be an interesting challenge. There is also a kata on this
# on codewars that I modified by code to be able to complete, but I think this return format is nicer
# so I stuck to using this. Already debugged, everything is functional with the exception of Ace low
# straights not being considered which was included in the initial design idea.

from itertools import combinations

hierarchy = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
sorting_key = {c: i for i, c in enumerate(hierarchy)}

def hand(hole_cards, community_cards):
    # making a list of lists containing every possible hand combination
    combos = list(list(x) for x in combinations(hole_cards+community_cards, 5))
    # replacing 10s with Ts
    for c in combos:
        for i, x in enumerate(c):
            if x[0] == '1':
                c[i] = 'T'+x[2]

    # sorts each hand to make looking for straights easier, sorted high to low
    combos = [sorted(i, key=lambda x: sorting_key[x[0]], reverse=True) for i in combos]

    # sort combos list, to make high card search more accurate
    combos = sorted(combos, key=lambda x: [sorting_key[c[0]] for c in x], reverse=True)

    # iterate through each possible hand combo and check against each possible hand, returning best hand
    for card_criteria in functions:
        for i in combos:
            test = card_criteria(i)
            if card_criteria(i)[1]:
                return test[0] + " " + str(i)

    # if high card, return highest high card combo
    return "High Card " + str(combos[0])

def is_straight_flush(cards):
    if is_flush(cards)[1] and is_straight(cards)[1]:
        return ("Straight Flush", True)
    return ("Straight Flush", False)

def is_quads(cards):
    for i in cards:
        if len([i[0] for j in cards if i[0] in j]) > 3:
            return ("Quads", True)
    return ("Quads", False)

def is_full_house(cards):
    # time complexity is bad but tolerable due to the small amount of cards
    for i in cards:
        if len([i[0] for j in cards if i[0] in j]) > 2:
            for k in cards:
                if len([k[0] for l in cards if k[0] in l]) > 1 and k[0] != i[0]:
                    return ("Full House", True)
    return ("Full House", False)

def is_flush(cards):
    suits = set(card[1] for card in cards)
    if len(suits) == 1:
        return ("Flush", True)
    return ("Flush", False)

def is_straight(cards):
    if not is_pair(cards)[1] and hierarchy.index(cards[0][0]) - hierarchy.index(cards[4][0]) == 4:
        return ("Straight", True)
    return ("Straight", False)

def is_trips(cards):
    for i in cards:
        if len([i[0] for j in cards if i[0] in j]) > 2:
            return ("Trips", True)
    return ("Trips", False)

def is_two_pair(cards):
    for i in cards:
        if len([i[0] for j in cards if i[0] in j]) > 1:
            for k in cards:
                if len([k[0] for l in cards if k[0] in l]) > 1 and k[0] != i[0]:
                    return ("Two Pair", True)
    return ("Two Pair", False)

def is_pair(cards):
    for i in cards:
        if len([i[0] for j in cards if i[0] in j]) > 1:
            return ("Pair", True)
    return ("Pair", False)

functions = [is_straight_flush, is_quads, is_full_house, is_flush, is_straight, is_trips, is_two_pair, is_pair]

print(hand(["K♠", "A♥"], ["J♣", "Q♥", "9♥", "2♥", "10♥"]))