class Warrior():
    ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]

    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = "Pushover"
        self.achievements = []
    

    def update(self):
        self.level = int((self.experience-self.experience%100)/100)
        self.rank = self.ranks[int((self.level-self.level%10)/10)]


    def training(self, training):
        if self.level >= training[2]:
            self.experience = min(self.experience + training[1], 10000)
            self.update()
            self.achievements.append(training[0])
            return training[0]
        return "Not strong enough"
    

    def battle(self, enemy_lvl):
        if enemy_lvl >= 1 and enemy_lvl <= 100:
            relative_lvl = enemy_lvl-self.level
            if relative_lvl >= 5 and self.rank != self.ranks[int((enemy_lvl-enemy_lvl%10)/10)]:
                return "You've been defeated"
            elif relative_lvl > 0:
                self.experience = min(20*relative_lvl*relative_lvl+self.experience, 10000)
                self.update()
                return "An intense fight"
            elif relative_lvl == 0:
                self.experience = min(10+self.experience, 10000)
                self.update()
                return "A good fight"
            elif relative_lvl == -1:
                self.experience = min(5+self.experience, 10000)
                self.update()
                return "A good fight"
            else:
                return "Easy fight"
        else:
            return "Invalid level"
            
