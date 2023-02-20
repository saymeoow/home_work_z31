import socket
import sys
import os

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5678

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv_sock.bind((SERVER_HOST, SERVER_PORT))
srv_sock.listen()

while True:
    try:
        print('Connection')
        client_connection, client_address = srv_sock.accept()

    except KeyboardInterrupt:
        srv_sock.close()
        print(end='\r')
        sys.exit()

    try:
        print('Connected:', client_address)

        while True:
            data = client_connection.recv(1024)
            print(f'Information received {data.decode("utf-8")}')
            print('Data processing')
            print('Sending to the client')
            data = data.decode('utf-8')
            data = data.encode('utf-8')
            client_connection.sendall(
                'Response: '.encode('utf-8') + data
            )
        else:
            print('No data from', client_address)
            break

    except KeyboardInterrupt:
        srv_sock.close()
        print(end='\r')
        sys.exit()
