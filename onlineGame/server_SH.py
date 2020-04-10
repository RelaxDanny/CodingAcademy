import socket
from _thread import *
import sys

server = "10.12.49.214"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#bridge

try: #에러가 일어났을때 체크하기위한 코드
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2) # unlimited player can join this game, but if 2, only 2 can enter
print("Waiting for a connection...")
print("server started!")


def read_pos(str):
    str = str.split(",") # ,형태로스트링을 나눠라 24, 30
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1]) # -. 24, 30 ->  "24, 30"

pos = [(0,0), (150,150)] 

def threaded_client(conn, currentPlayer):
    conn.send(str.encode(make_pos(pos[currentPlayer])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[currentPlayer] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Recieved:", data)
                print("Sending:", reply)

            conn.sendall(str.encode(reply)) #encode 해서 보내고 decode 해서 받는다
        except:
            break
    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1