import socket, select

print("Hi")
clientId = 0 # increment for each unique client; generate id. TODO: Would be better if the client could provide us a unique id somehow
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname() # Debating do we run this or not
print("hostname: " + hostname)
server.setblocking(0)
server.bind(('', 4000))
server.listen(5)

clients = []
while True:
    Connections, wlist, xlist = select.select([server], [], [], 0.05)

    for Connection in Connections:
        client, Informations = Connection.accept()
        Connection.setblocking(0)
        clients.append(client)

    clientsList = []
    try:
        clientsList, wlist, xlist = select.select(clients, [], [], 0.05)
    except select.error:
        pass
    else:
        for clientInList in clientsList:
            try:
                data = clientInList.recv(4)
                if (data):
                    value = int.from_bytes(data, byteorder='little')
                    if (clientId == 0):
                        print(value)
                        clientId = 1
            except:
                pass


clientInList.close()
server.close()