import socket

class network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.12.49.214"
        self.port = 5555
        self.addr = (self.server, self.port) #ip 주소, 포트 --> 튜플
        self.pos = self.connect() # id = connect를 통한 return 값
        
    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr) #
            return self.client.recv(2048).decode() # String 
        except:
            pass

    def send(self, data):
        try: 
            self.client.send(str.encode(data)) # encode 누군가에게 보내기 위한 준비! 포장꾸러미
            return self.client.recv(2048).decode() # decode 포장꾸러미 풀기!
        except socket.error as e:
            print(e)
