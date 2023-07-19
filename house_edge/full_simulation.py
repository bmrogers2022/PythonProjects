# modules for game
import tkinter
import random

# cards (double deck)
card_types = "A23456789TJQK"
double_deck = [x for i in range (2*4) for x in card_types]
six_deck = [x for i in range (6*4) for x in card_types]
money = 500

active_deck = double_deck
random.shuffle(active_deck)

# one card burned at beginning
active_deck.pop()

# set up game
hands = [[]]
dealer_hand = []
last_hand = dealer_hand
your_last_hand = hands
current_hand = 0
bet_size = 25

# reset game
def set_hand():
    global hands
    global dealer_hand
    global current_hand
    global last_hand
    global your_last_hand
    last_hand = dealer_hand
    your_last_hand = hands
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
    global bet_size
    bet.focus_set()
    bet_size = int(bet.get()) if bet.get().isdigit() else 25
    deal_player_card()
    deal_dealer_card()
    deal_player_card()
    deal_dealer_card()

# player splits hand
def split():
    global current_hand
    if hands[current_hand][0] != hands[current_hand][1]:
        return None
    hands.append([])
    hands[-1].append(hands[current_hand].pop())
    deal_player_card()
    current_hand += 1
    deal_player_card()
    current_hand -= 1
    update()

# player hits hands
def hit():
    global current_hand
    deal_player_card()
    if point_total() > 21:
        current_hand += 1
        if current_hand == len(hands):
            end_hand()
    update()

# player stands
def stand():
    global current_hand
    current_hand += 1
    if current_hand == len(hands):
        end_hand()
    update()

def dealer_score():
    global dealer_hand
    soft = False
    total = 0
    hand_sorted = dealer_hand
    hand_sorted.sort(key=lambda x:card_types.index(x), reverse=True)
    for i in hand_sorted:
        if i != "A":
            total += min(card_types.index(i) + 1, 10)
        else:
            if total + 11 > 21:
                total += 1
            else:
                total += 11
                soft = True
    if total > 17:
        return total
    if total == 17 and not soft:
        return total
    else:
        deal_dealer_card()
        return dealer_score()

# sets hand deals hand
def end_hand():
    global current_hand
    global money
    for i in range(len(hands)):
        current_hand = i
        points = point_total()
        current_bet_size = min(bet_size, money)
        if points > 21:
            money -= current_bet_size
        elif points == 21 and len(hands[current_hand]) == 2:
            money += current_bet_size*3/2
        else:
            dealer_point_total = dealer_score()
            if dealer_point_total > 22:
                money += current_bet_size
            elif points > dealer_point_total:
                money += current_bet_size
            elif dealer_point_total == 22:
                pass
            elif dealer_point_total == points:
                pass
            else:
                money -= current_bet_size

    set_hand()
    dealer_last.config(text=f"Dealer's last hand = {last_hand}")
    your_last.config(text=f"Your last hand = {your_last_hand}")
    deal_hand()
    

# updates GUI
def update():
    hand_label.config(text=f"Current hand = {current_hand+1}, Current value = {point_total()}")
    player_hand_labels.config(text=f"hands = {hands}")
    dealer_label.config(text=f"Dealer hand = {dealer_hand[0]}, X")
    money_label.config(text=f"Money = {money}")

    
# find point total
def point_total():
    total = 0
    hand_sorted = hands[current_hand]
    hand_sorted.sort(key=lambda x:card_types.index(x), reverse=True)
    for i in hand_sorted:
        if i != "A":
            total += min(card_types.index(i) + 1, 10)
        else:
            if total + 11 > 21:
                total += 1
            else:
                total += 11
    return total

# set up GUI
root = tkinter.Tk()
# set title
root.title("House Odds")
# set screen size
root.geometry("800x800")
# bet enter
bet = tkinter.Entry(root)
bet.pack()
bet.focus_set()

# start the game
deal_hand()

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
# label money
money_label = tkinter.Label(root, text=f"Money = {money}")
money_label.place(x=350, y = 600)
# label dealer's hand
dealer_label = tkinter.Label(root, text=f"Dealer hand = {dealer_hand[0]}, X")
dealer_label.place(x=350, y=50)
# label dealer's last hand
dealer_last = tkinter.Label(root, text="")
dealer_last.place(x=320, y=150)
# label your last hand
your_last = tkinter.Label(root, text="")
your_last.place(x=320, y=250)
# your hand(s)
player_hand_labels = tkinter.Label(root, text=f"hands = {hands}")
player_hand_labels.place(x=350, y=400)

# start GUI
root.mainloop()
