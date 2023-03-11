'''
Autodraft on ESPN's fantasy app and fantasy apps in general are infamously
very awful. The main issue with it is that it defaults to Non-PPR no superflex
draft order priority so lots of the picks make little to no sense in teams with different
settings. I made this program so that I could run autodraft with the correct draft
positions (cdp) and improve autodraft for the people in my league if they can't make it.
fill in cdp dictionary to optimized draft order for your format and run the program.
I plan to make modifications to the program to make it more user friendly once it is
closer to draft time, but it is technically functional right now.
'''

with open('cdp.txt') as file:
    info = [x.strip() for x in file.readlines()]

draft_order = []

# enter one player name on each line of the cdp text file
cdp = {}

def best_pick(cdp):
    return cdp[min(cdp.keys())]

def make_cdp(info):
    cdp = {}
    for i in range(len(info)):
        cdp[i+1] = info[i]
    return cdp

cdp = make_cdp(info)
print(cdp)

while cdp:
    print(f'available picks: {cdp}')
    print(f'best pick: {best_pick(cdp)}')
    draft_order.append(cdp.pop(int(input("What CDP player was picked? "))))

print(draft_order)

# makes text file displaying the order of the draft to save for later use
with open('draft_order.txt', 'w+') as picks:
    for i in range(len(draft_order)):
        picks.write(f'{i+1}: {draft_order[i]}\n')
        