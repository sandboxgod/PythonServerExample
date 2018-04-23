import socket, select, sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname() # Not using atm
print("hostname: " + hostname)
server.setblocking(0)
server.bind(('', 4000))
server.listen(5)

inputs = [server]
outputs = []

while inputs:
    readable, writable, exceptional = select.select(
        inputs, outputs, inputs, 0)
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            connection.setblocking(0)
            inputs.append(connection)
        else:
            try:
                data = s.recv(4)
                if data:
                    value = int.from_bytes(data, byteorder='little')
                    print(value)
                    if s not in outputs:
                        outputs.append(s)
                else:
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()
            except:
                pass

    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

