class partyAnimal:
    x = 0
    def __init__(self, z):
        self.name = z
        print(self.name,'Constructor initialized')
    def party(self):
        self.x = self.x+1
        print('Value: ',self.x)

class FootballFan(partyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points+7
        self.party()
        print(self.name,"points",self.points)

j = FootballFan("Jim")
j.touchdown()
j.touchdown()
