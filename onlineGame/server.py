import socket
from _thread import *
from player import Player
import pickle
from game import Game

server = "10.12.49.93"
port = 5484

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")
#unlimited connection !! 
#it will have list that contain bunch of games that is accessed by the users' ip

connected = set()
games = {} #dictionary will store out games and game object as value
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount #when someone leaves, we should keep traking of the clients' games
    conn.send(str.encode(str(p))) # player 1 or 0

    reply = ""
    while True:
        data = conn.recv(4096).decode()

        if gameId in games:
            game = games[gameId] # in the while loop, we continuously check if the games is ON.
            if not data:
                break
            else:
                if data == "reset":
                    game.reset()
                elif data != "get":
                    game.play(p, data) #data contains the move
                
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
    idCount -= 1 #client 수 한명씩 빼기 애들 나가면
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    #after the connection:
    idCount += 1 #keep track of the number of connections
    p = 0
    gameId = (idCount - 1)//2 #every two people that is connected, they will be binded. 
    #10명이면 5게임이 되지만, 7명일 경우 한게임을 더 만들어야함.
    if idCount % 2 == 1: #if 홀수
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else: 
        #we don't have to create games
        games[gameId].ready = True #게임준비완료
        p = 1 #player = 1
        start_new_thread(threaded_client, (conn, p, gamId))
