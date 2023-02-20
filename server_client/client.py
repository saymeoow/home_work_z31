import os
import socket
import sys


SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5678

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.settimeout(1)
client_sock.connect((SERVER_HOST, SERVER_PORT))

stdin = sys.stdin
stdout = sys.stdout

while True:
    try:
        for line in stdin:
            if 'exit' == line.strip():
                sys.exit()

            else:
                msg = line
                client_sock.sendall(msg.encode('utf-8'))

                amount_received = 0
                amount_expected = len(msg)

                while amount_received < amount_expected:

                    data = client_sock.recv(1024)
                    amount_received += len(data)
                    message = data.decode('utf-8')
                    message = stdout.write(msg)

    except KeyboardInterrupt:
        client_sock.close()
        print(end='\r')
        sys.exit()
