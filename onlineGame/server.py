import socket
from _thread import *
import sys

server = "10.12.49.214"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # This is always used for the socket!  Socket이다!

try: #error가 일어났을때 체크하기 위한 코드
    s.bind((server, port)) #bind = connect, socket 서버와 포트에 연결해라
except socket.error as e: 
    str(e)

s.listen(2) #default = unlimited players can join this game. 만약 리슨을 2로한다면 우리가 하고 있는 게임에 only 2명만 입장 가능.
print("Waiting for a connection, Server Started.")

def threaded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048) # 2^11 만큼의 data먼저 받는데 -> 0101010100
            reply = data.decode("utf-8") #사람의 언어 utf-8 영어!! -> 김영호
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))  #김영호 -> ajkdnqjkwdnqjkwf
        except:
            break

while True:
    conn, addr = s.accept() #accept any incoming connections 
    print("Connected to : ", addr)

    start_new_thread(threaded_client, (conn, ))

#쓰레드 -> 