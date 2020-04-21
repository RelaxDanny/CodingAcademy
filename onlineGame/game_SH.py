# 가위 바위 보 게임

class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id #each client has unique id.
        self.moves = [None, None] #[Rock, Paper]
        self.wins = [0, 0] #p1, p2
        self.ties = 0
    
    def get_player_move(self, p):
        # p : [0,1]
        return self.moves[p]
    
    def player(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else: #player == 1
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went # 1 or 0 
        #True and True = True
        #True and False = False
        #False and True = False
        #False and False = False
    
    def winner(self):# 9가지 경우의수
        p1 = self.moves[0].upper()[0] #moves  Rock.upper() str.upper() =>모든걸 대문자로 바꿈
        p2 = self.moves[1].upper()[0] #R, P, S

        winner = -1 #Tie p1이 이기면은 0, p2가 이기면 1으로 한다.
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
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

