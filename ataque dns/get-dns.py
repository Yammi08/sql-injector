from socketserver import *
from pwn import *


class myUDPServer(BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print(f"{self.client_address[0]} wrote:")
        print('socket: ',socket,'data: ' ,data)
        socket.sendto(data, self.client_address)
def main():
    port, ip = 53,'0.0.0.0';
    with UDPServer((ip,port),myUDPServer) as server:
        server.serve_forever();
    T
main()

