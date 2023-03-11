'''
I saw somebody playing a game where they would try making a team based on players
drafted from random teams and wanted to play myself, so I made a program that allowed
me to do it
'''

import random

nfl_teams = ['Cardinals', 'Falcons', 'Ravens', 'Bills', 'Panthers', 'Bears', 'Bengals', 'Browns', 'Cowboys', 'Broncos', 'Lions', 
            'Packers', 'Texans', 'Colts', 'Jaguars', 'Chiefs', 'Raiders', 'Chargers', 'Rams', 'Dolphins', 'Vikings', 'Patriots',
            'Saints', 'Giants', 'Jets', 'Eagles', 'Steelers', '49ers', 'Seahawks', 'Buccaneers', 'Titans', 'Commanders']

class Team:
    def __init__(self, QB=None, RB1=None, RB2=None, WR1=None, WR2=None, WR3=None, TE=None, D_ST=None, Coach=None, team=[]):
        self.QB = QB
        self.RB1 = RB1
        self.RB2 = RB2
        self.WR1 = WR1
        self.WR2 = WR2
        self.WR3 = WR3
        self.TE = TE
        self.D_ST = D_ST
        self.Coach = Coach
        self.team = team
        self.left = {'QB': 1, 'RB': 2, 'WR': 3, 'TE': 1, 'D/ST': 1, 'Coach': 1}

    def update(self):
        self.team = [x for x in [self.QB, self.RB1, self.RB2, self.WR1, self.WR2, self.WR3, self.TE, self.D_ST, self.Coach] if x != None]
    
    def reset(self):
        print("You're a cheater, team reset.")
        self.__init__()

    def new_add(self):
        team_criteria = random.choice(nfl_teams)
        print('Positions to fill: ' + ' | '.join([x for x in self.left.keys() if self.left[x] > 0]))
        pos = input('What pos from the ' + team_criteria + '? : ')
        if pos != 'd/st' and pos != 'D/ST':
            player = input('What player? : ')
        if pos == 'wr' or pos == 'WR':
            if not self.WR1:
                self.WR1 = player
            elif not self.WR2:
                self.WR2 = player
            elif not self.WR3:
                self.WR3 = player
            else:
                self.reset()
            self.left['WR'] -= 1
        elif pos == 'rb' or pos == 'RB':
            if not self.RB1:
                self.RB1 = player
            elif not self.RB2:
                self.RB2 = player
            else:
                self.reset()
            self.left['RB'] -= 1
        elif pos == 'qb' or pos == 'QB':
            if not self.QB:
                self.QB = player
            else:
                self.reset()
            self.left['QB'] -= 1
        elif pos == 'te' or pos == 'TE':
            if not self.TE:
                self.TE = player
            else:
                self.reset()
            self.left['TE'] -= 1
        elif pos == 'd/st' or pos == 'D/ST':
            if not self.D_ST:
                self.D_ST = team_criteria + ' D/ST'
            else:
                self.reset()
            self.left['D/ST'] -= 1
        elif pos == 'coach' or pos == 'Coach':
            if not self.Coach:
                self.Coach = player
            else:
                self.reset()
            self.left['Coach'] -= 1
        else:
            print('invalid pos')

drafted_team = Team()
while len(drafted_team.team) < 9:
    drafted_team.new_add()
    drafted_team.update()
    print(drafted_team.team)
print('Well done! Final team = ' + ' | '.join(drafted_team.team))
