import socket, select, sys, queue

print("Hi")
clientId = 0 # increment for each unique client; generate id. TODO: Would be better if the client could provide us a unique id somehow
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname() # Debating do we run this or not
print("hostname: " + hostname)
server.setblocking(0)
server.bind(('', 4000))
server.listen(5)

inputs = [server]
outputs = []
message_queues = {}

while inputs:
    readable, writable, exceptional = select.select(
        inputs, outputs, inputs, 0)
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(4)
            if data:
                value = int.from_bytes(data, byteorder='little')
                print(value)
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]

    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            outputs.remove(s)
        else:
            s.send(next_msg)

    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]

