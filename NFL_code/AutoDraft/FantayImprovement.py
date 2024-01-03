'''
New plan for this year is to create player projections using posted vegas odds on player
props. Goal is to have customizable league settings, and perhaps a website to use these
player props to create a statistically optimal drafting plan. Last model was successful,
landing a 1st 2nd and 3rd place in the three 10 man leagues it was used in with profits of
1200 dollars. Hopefully we can find even more success by using tensorflow to analyze relative
positional value for different league settings more precisely and create a unique profitable
autodrafter for all possible settings
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

picks_count = "0"

while not picks_count.isdigit() or int(picks_count) < 1:
    picks_count = input("How many picks per team in your league: ")

your_league = League(int(picks_count))

team_count = "0"

while not team_count.isdigit() or int(team_count) < 1:
    team_count = input("How many teams are in your league: ")

WR_count = "-1"

while not WR_count.isdigit() or int(WR_count) < 0:
    WR_count = input("How many WRs must you start")

RB_count = "-1"

while not RB_count.isdigit() or int(RB_count) < 0:
    RB_count = input("How many RBs must you start")

QB_count = "-1"

while not QB_count.isdigit() or int(QB_count) < 0:
    QB_count = input("How many QBs must you start (if superflex enter 2)")

TE_count = "-1"

while not TE_count.isdigit() or int(TE_count) < 0:
    TE_count = input("How many TEs must you start")

WRTERB_count = "-1"

# TODO: possibly add other flex options in the future
while not WRTERB_count.isdigit() or int(WRTERB_count) < 0:
    WRTERB_count = input("How many flex spots for WR/RB/TE do you have?")

ppr = "-1"
while not ppr.isdigit() or -1 < int(ppr) < 3:
    ppr = input("Input 0 for non ppr, 1 for half ppr, and 2 for ppr")

passing_TD = "4"
while not passing_TD.isdigit(): # technically possible some leagues making passing TDS negative
    passing_TD = input("how many points per passing TD")

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

"""
TODO: hopefully find some sort of way to import vegas projections of yards, receptions, TDS etc.
if there isn't an easy way to do it I can manually input the data but the goal is for projections
to be live
"""  
