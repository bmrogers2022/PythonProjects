# modules for game
import tkinter
import random

# cards (double deck)
card_types = "A23456789TJQK"
double_deck = [x for i in range (2*4) for x in card_types]
six_deck = [x for i in range (6*4) for x in card_types]

active_deck = double_deck
random.shuffle(active_deck)

# one card burned at beginning
active_deck.pop()

# set up game
hands = [[]]
dealer_hand = []
current_hand = 0

# reset game
def set_hand():
    global hands
    global dealer_hand
    global current_hand
    hands = [[]]
    dealer_hand = []
    current_hand = 0

# deal hands
def deal_player_card():
    hands[current_hand].append(active_deck.pop())

# deal player cards
def deal_dealer_card():
    dealer_hand.append(active_deck.pop())

# deal starting hands
def deal_hand():
    deal_player_card()
    deal_dealer_card()
    deal_player_card()
    deal_dealer_card()

# player splits hand
def split():
    if hands[current_hand][0] != hands[current_hand][1]:
        return None
    hands.append([])
    hands[-1].append(hands[current_hand].pop())
    deal_player_card(-1)
    deal_player_card()
    update()

# player hits hands
def hit():
    global current_hand
    deal_player_card()
    if point_total() > 21:
        current_hand += 1
        if current_hand == len(hands):
            set_hand()
            deal_hand()
    update()

# player stands
def stand():
    global current_hand
    current_hand += 1
    if current_hand == len(hands):
        set_hand()
        deal_hand()
    update()

# updates GUI
def update():
    hand_label.config(text=f"Current hand = {current_hand+1}, Current value = {point_total()}")
    player_hand_labels.config(text=f"hands = {hands}")
    dealer_label.config(text=f"Dealer hand = {dealer_hand[0]}, X")
    
# find point total
def point_total():
    total = 0
    hand_sorted = hands[current_hand]
    hand_sorted.sort(key=lambda x:card_types.index(x))
    for i in hand_sorted:
        if i != "A":
            total += min(card_types.index(i) + 1, 10)
        else:
            if total + 11 > 21:
                total += 1
            else:
                total += 11
    return total

# start the game
deal_hand()


# set up GUI
root = tkinter.Tk()
# set title
root.title("House Odds")
# set screen size
root.geometry("800x800")
# button to hit
hit_btn = tkinter.Button(root, text="Hit", command=hit)
hit_btn.pack(side="left")
# button to stand
stand_btn = tkinter.Button(root, text="Stand", command=stand)
stand_btn.pack(side="right")
# button to split
split_btn = tkinter.Button(root, text="Split", command=split)
split_btn.pack(side="left")
# label hand you are on
hand_label = tkinter.Label(root, text=f"Current hand = {current_hand+1}, Current value = {point_total()}")
hand_label.place(x=310, y=700)
# label dealer's hand
dealer_label = tkinter.Label(root, text=f"Dealer hand = {dealer_hand[0]}, X")
dealer_label.place(x=350, y=50)
# your hand(s)
player_hand_labels = tkinter.Label(root, text=f"hands = {hands}")
player_hand_labels.place(x=350, y=400)
# start GUI
root.mainloop()
