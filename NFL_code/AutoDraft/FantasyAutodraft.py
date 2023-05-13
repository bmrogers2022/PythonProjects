'''
Autodraft on ESPN's fantasy app and fantasy apps in general are infamously
very awful. The main issue with it is that it defaults to PPR no superflex
draft order priority so lots of the picks make little to no sense in teams with different
settings. To use, fill in cdp dictionary to optimized draft order for your format and run 
the program.
'''

with open('cdp.txt') as file:
    old_info = [x.strip() for x in file.readlines()]

info = []
for x in old_info:
    player_name = ""
    i = 0
    while x[i] != "(":
        player_name += x[i]
        i+= 1
    info.append(player_name)

draft_order = []

# enter one player name on each line of the cdp text file
cdp = {}

def best_picks(cdp, players):
    players_returned = {}
    for key in cdp.keys():
        if len(players_returned) < players:
            players_returned[key] = cdp[key]
    return players_returned

def make_cdp(info, length_of_draft):
    cdp = {}
    for i in range(length_of_draft):
        cdp[i+1] = info[i]
    return cdp

cdp = make_cdp(info, 100)
sorted_by_rel_val = {k: v for k, v in sorted(cdp.items(), key=lambda player: player[1], reverse=True)}
print(cdp)

while cdp:
    print(f'available picks: {cdp}')
    print(f'best five picks: {best_picks(cdp, 5)}')
    print(f'best pick: {best_picks(cdp, 1)}')
    player = "Start"
    while not player.isdigit():
        player = input("\n---------------------------------------\nUse a number!\nWhat CDP player was picked? ")
        if player == "end":
            break
    if player == "end":
        break
    player = int(player)
    while player not in cdp:
        while not player.isdigit():
            player = input("\n---------------------------------------\nUse a number!\nWhat CDP player was picked? ")
        player = int(player)
    draft_order.append(cdp.pop(player))

print(draft_order)

# makes text file displaying the order of the draft to save for later use
with open('draft_order.txt', 'w+') as picks:
    for i in range(len(draft_order)):
        picks.write(f'{i+1}: {draft_order[i]}\n')
        
