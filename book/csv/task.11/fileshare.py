import threading
import socket
import json


class Main:
    def __init__(self) -> None:
        self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 4545
        # self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket = socket.socket()
        self.socket2 = socket.socket()
    
    def server(self) -> None:

        self.socket.bind((self.IP, self.PORT))
        print(f'User {self.IP}    :Online:')

        self.socket.listen(1)
        print('server started')
        while True:
        
            c, addr = self.socket.accept()

            data = json.loads(c.recv(5000).decode())
            with open(f'{data.get("filename")}', 'w') as file:
                file.write(data.get('text'))
            
            print(f'{data.get("ip")} = {data.get("filename")}')

            c.close()

            

    def client(self) -> None:

        print('client started')
        while True:
            
            try:
                msg = input('~').split()
                IP = msg[0]

                socket2 = socket.socket()
                
                socket2.connect((IP, self.PORT))

                data = {
                    'ip': self.IP,
                    'filename': f'{self.IP.replace(".", "-")}-{msg[1]}',
                    'text': open(msg[1]).read()
                }
                socket2.sendall(
                    json.dumps(data).encode()
                )

                socket2.close()
            except Exception as e:
                print(e)


session = Main()

thread1 = threading.Thread(target=session.server)
thread2 = threading.Thread(target=session.client)

thread1.start()
thread2.start()