import socket
from _thread import *
from player import Player
import pickle

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


players = [Player(0,0,50,50,(255,0,0)), Player(100,100, 50,50, (0,0,255))]

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

        if gameId in games:
            game = games[gameId] # in the while loop, we continuously check if the games is ON.
            if not data:
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
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
