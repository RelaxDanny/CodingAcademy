 
class Game:
    
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id #each client has unique id.
        self.moves = [None, None] 
        self.wins = [0, 0] #p1, p2
        self.ties = 0

    def get_player_move(self, p):
        # p : [0,1]
        # return : Move 
        return self.moves[p]

    def player(self, player, move): #update the player's move
        self.moves[player] = move
        if player == 0:
            p1Went = True
        else:
            self.p2Went = True
    def connected(self):
        return self.ready
    
    def bothWent(self):
        return self.p1Went and self.p2Went
    
    def winner(self):#9 possible case 3x3
        p1 = self.moves[0].upper()[0] #first letter of the move Rock, Paper, Scissors -> R, P, S
        p2 = self.moves[1].upper()[0]

        winner = -1#there could be no winner when they tie 
        if p1 =="R" and p2 =="S":
            winner = 0
        elif p1 =="S" and p2 == "R":
            winner = 1
        elif p1 =="P" and p2 =="R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "P" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        
        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False

