import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('127.0.0.1', 4000))

while True:
    data = (2147483647).to_bytes(4,byteorder='little')
    server.send(data)

server.close()
