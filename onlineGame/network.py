import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.12.49.24"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            #return pickle.loads(self.client.recv(2048)) pickle을 풀지는 않고 이번엔 디코드 할거임
            return self.client.recv(2048).decode() #시작하자 받는 정보는 플레이어의 정보이다 0 또는 1 (1p 또는 2p)
            #그럼 커넥트는 플레이어가 누구인지를 리턴함
        except:
            pass

    def send(self, data):
        try:
            # self.client.send(pickle.dumps(data))
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)