import socket
from _thread import *
from player import Player
import pickle
from game_SH import Game

server = "10.12.49.24"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#bridge #TCP

try: #에러가 일어났을때 체크하기위한 코드
    s.bind((server, port)) 
except socket.error as e:
    str(e)

s.listen() # unlimited player can join this game

print("Waiting for a connection...")
print("server started!")

connected = set()
games = {}
idCount = 0 # client가 들어올때마다 1씩 올라가는 counter 

def threaded_client(conn, p, gameId):
    global idCount #When some leaves, it counts how many clients are left.
    conn.send(str.encode(p))
    reply = "" # "" << 값이 끊겨
    
    while True:
        data = conn.recv(4096).decode() #Client  = USER = 게임에 들어온사람으로 부터 받은 값은 = data

        if gameId in games: # games안에 gameId가 있다면. 
            game = games[gameId]
            if not data:
                break
            else:
                if data == "reset":
                    game.reset()
                elif data != "get": # 코딩에서 ! 는 NOT을 의미함. Not equal
                    game.play(p, data)

                reply = game
                conn.sendall(pickle.dumps(reply))
        else:
            break     
    print("Lost Connection")
    try: 
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()
    
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    #after the connection
    idCount += 1
    p = 0
    gameId = (idCount - 1)//2  #각 두명의 플레이어가 접속 했을때, 둘을 합쳐줘라. 4.5 => 5
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new Game")
    else:
        #짝수면 이미 Pair가있다는것.
        games[gameId].ready = True
        p = 1 #player = 1
    #10 // 3 = 3
    #10 / 3 = 3.3333333
    start_new_thread(threaded_client, (conn, p, gameId))
