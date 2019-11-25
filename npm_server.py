from socket import socket, AF_INET, SOCK_STREAM
import random
import os

port = 3443
buffer_size = 1024
package_names = os.listdir('/volatile/m139t745/npm-packages/')
random.shuffle(package_names)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', port))
server_socket.listen(100)

while True:

    # listen for any messages from clients
    connection_socket, addr = server_socket.accept()
    message = connection_socket.recv(buffer_size).decode('utf8')
    
    # if client is requesting a new package
    if message == 'request':
        if len(package_names) == 0:
            response = 'no packages remaining'
        else:
            response = package_names.pop(0)

        connection_socket.send(response.encode('utf8'))
        connection_socket.close()
