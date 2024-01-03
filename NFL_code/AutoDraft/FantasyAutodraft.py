'''
Autodraft on ESPN's fantasy app and fantasy apps in general are infamously
very awful. The main issue with it is that it defaults to PPR no superflex
draft order priority so lots of the picks make little to no sense in teams with different
settings. To use, fill in cdp dictionary to optimized draft order for your format and run 
the program.
'''

# setting up league class
class League:

    def __init__(self, picks):
        self.teams = []
        self.team_count = 0
        self.picks = picks
    
    def updateCount(self):
        team_count = len(self.teams)
    
# saving data of all teams in league
class Team:

    def __init__(self, league, name):
        self.wrCount = 0
        self.rbCount = 0
        self.teCount = 0
        self.qbCount = 0
        self.dstCount = 0
        self.kCount = 0
        self.league = league
        self.name = name
        self.picks_left = league.picks
        self.players = []

    def addPlayer(self, player):
        '''
        if player is not on the list of pickable players but is still picked,
        take pick away and move on
        '''
        if player == 0:
            self.picks_left -= 1
            return 0

        self.players.append(player)

        if "RB" in player:
            self.rbCount += 1
        elif "WR" in player:
            self.wrCount += 1
        elif "TE" in player:
            self.teCount += 1
        elif "QB" in player:
            self.qbCount += 1
        elif "DST" in player:
            self.dstCount += 1
        elif "K" in player:
            self.kCount += 1
        self.picks_left -= 1

    def display(self):
        team_name = f"\nTeam: {self.name}"
        info1 = f"\nPlayers: {self.players}\nQBs: {self.qbCount}\nRBs: {self.rbCount}\n"
        info2 = f"WRs: {self.wrCount}\nTEs: {self.teCount}\nDSTs:{self.dstCount}\nKs: {self.kCount}"
        print(team_name+info1+info2)

current_file = "cdp_updated.txt"

with open('cdp_updated.txt') as file:
    old_info = [x.strip() for x in file.readlines()]

picks_count = "0"

while not picks_count.isdigit() or int(picks_count) < 1:
    picks_count = input("How many picks per team in your league: ")

your_league = League(int(picks_count))

team_count = "0"

while not team_count.isdigit() or int(team_count) < 1:
    team_count = input("How many teams are in your league: ")

# Optional feature to add team names
name_bool = input("Do you want to name teams? Y/N")
if name_bool in "Yy":
    for i in range(int(team_count)):
        team_name = input(f"Enter team {i+1}s name: ")
        your_league.teams.append(Team(your_league, team_name))
else:
    for i in range(int(team_count)):
        team_name = f"Team {i+1}"
        your_league.teams.append(Team(your_league, team_name))

your_league.team_count = int(team_count)

info = []
for x in old_info:
    player_name = ""
    i = 0
    while x[i] != "(":
        player_name += x[i]
        i+= 1
    while x[i] != "\t":
        i += 1
    while x[i] == "\t":
        i += 1
    player_name += " "
    while x[i] != "\t":
        player_name += x[i]
        i += 1
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

cdp = make_cdp(info, 300)
picked  = set()
sorted_by_rel_val = {k: v for k, v in sorted(cdp.items(), key=lambda player: player[1], reverse=True)}
print(cdp)

teams_pick = 0
teams_reverse = False

while cdp and your_league.teams[-1].picks_left > 0:
    print(f'available picks: {cdp}')
    print(f'best five picks: {best_picks(cdp, 5)}')
    print(f'best pick: {best_picks(cdp, 1)}')
    player = "Start"
    while not player.isdigit() or int(player) in picked:
        player = input("\n---------------------------------------\nUse a number!\nWhat CDP player was picked? ")
        if player == "end":
            break
    if player == "end":
        break
    player = int(player)
    while player not in cdp:
        player = str(player)
        while not player.isdigit() or int(player) not in cdp:
            player = input("\n---------------------------------------\nUse a number!\nWhat CDP player was picked? ")
            if player == "end":
                break
        player = int(player)
    picked.add(player)
    official_pick = cdp.pop(player)
    
    draft_order.append(official_pick)

    # this is for non snake draft
    # your_league.teams[teams_pick % your_league.team_count].addPlayer(official_pick)
    # teams_pick += 1

    # this is for snake draft

    your_league.teams[teams_pick].addPlayer(official_pick)

    if teams_reverse:
        teams_pick -= 1
    else:
        teams_pick += 1

    if teams_pick == your_league.team_count:
        teams_pick = your_league.team_count - 1
        teams_reverse = True
    elif teams_pick == -1:
        teams_pick = 0
        teams_reverse = False

    

print(draft_order)
for i in your_league.teams:
    i.display()

# makes text file displaying the order of the draft to save for later use
with open('draft_order.txt', 'w+') as picks:
    for i in range(len(draft_order)):
        picks.write(f'{i+1}: {draft_order[i]}\n')
        
