import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('127.0.0.1', 4000))
count = 0
while True:
    data = (count).to_bytes(4,byteorder='little')
    server.send(data)
    count += 1

server.close()
