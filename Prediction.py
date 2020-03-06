'''
By: Emmanuel Efewongbe
This program simulates a soccer team, using the concept of object oriented programming
'''

class Player(object):
    def __init__(self, PlayerAtt = None):
        self.PlayerAtt = {}
        self.PlayerAtt['name'] = PlayerAtt['name']
        self.PlayerAtt['number'] = PlayerAtt['number']
        self.PlayerAtt['pace'] = PlayerAtt['pace']
        self.PlayerAtt['shot'] = PlayerAtt['shot']
        self.PlayerAtt['pass'] = PlayerAtt['pass']
        self.PlayerAtt['dribble'] = PlayerAtt['dribble']
        self.PlayerAtt['defence'] = PlayerAtt['defence']
        self.PlayerAtt['physique'] = PlayerAtt['physique']

    def updatePace(cls, newPace):
        cls.PlayerAtt['pace'] = newPace
    def updateShot(cls, newShot):
        cls.PlayerAtt['shot'] = newShot
    def updatePass(cls, newPass):
        cls.PlayerAtt['pass'] = newPass
    def updateDribble(cls, newDribble):
        cls.PlayerAtt['dribble'] = newDribble
    def updateDefence(cls, newDefence):
        cls.PlayerAtt['defence'] = newDefence
    def updatePhysique(cls, newPhysique):
        cls.PlayerAtt['physique'] = newPhysique

    def printAtt(self):
        return("Name: {}\nNumber: {}\nPace: {}\nShot: {}\nPass: {}\nDribble: {}\nDefence: {}\nPhysique: {}\n ".format(self.PlayerAtt['name'],
              self.PlayerAtt['number'],
              self.PlayerAtt['pace'],
              self.PlayerAtt['shot'],
              self.PlayerAtt['pass'],
              self.PlayerAtt['dribble'],
              self.PlayerAtt['defence'],
              self.PlayerAtt['physique']))


class Coach(object):
        coach = {'name': None, 'rating': None}

        def __init__(self, coach):
            self.coach['name'] = coach['name']
            self.coach['rating'] = coach['rating']

        @classmethod
        def update(cls, newName):
            cls.coach['name'] = newName

        def updateRating(cls, newRating):
            cls.coach['rating'] = newRating

        def printCoach(cls):
            return ('Coach Name: {}\nCoach Rating: {}'.format(cls.coach['name'], cls.coach['rating']))


class Team(object):

    def __init__(self, name, coach):
        players = None
        self.name = name
        self.coach = coach
        if players is not None:
            self._players = list(players)
        else:
            self._players = []

    def add_player(self, newPlayer):
        if isinstance(newPlayer, Player):
            self._players.append(newPlayer)

    def printTeam(self):
       print("Team name: {} \n".format(self.name))
       print(self.coach.printCoach())
       print("\nPlayers: ")
       for player in self._players:
           print(player.printAtt())



#Program Testing
myCoach = {'name': 'Pep Guardiola', 'rating': 99}
coach = Coach(myCoach)
Barca = Team('Barcelona FC', coach)


myPlayer1 = Player({'name': 'Messi Lionel', 'number': 10, 'pace': 88, 'shot': 92, 'pass': 94, 'dribble': 88, 'defence': 45, 'physique': 49})
myPlayer2 = Player({'name': 'Lui Suarez', 'number': 9, 'pace': 88, 'shot': 92, 'pass': 94, 'dribble': 88, 'defence': 45, 'physique': 49})
myPlayer3 = Player({'name': 'Ousmane Dembele', 'number': 11, 'pace': 88, 'shot': 92, 'pass': 94, 'dribble': 88, 'defence': 45, 'physique': 49})
myPlayer4 = Player({'name': 'Atoinne Griezmann', 'number': 13, 'pace': 88, 'shot': 92, 'pass': 94, 'dribble': 88, 'defence': 45, 'physique': 49})

Barca.add_player(myPlayer1)
Barca.add_player(myPlayer2)
Barca.add_player(myPlayer3)
Barca.add_player(myPlayer4)
Barca.printTeam()