import socket
import time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.setblocking(False)

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)

print(f"Listening on port {SERVER_PORT} ...")

while True:
    try:
        client_socket, client_address = server_socket.accept()
        print(client_socket)
        print(client_address)
    except:
        time.sleep(1)
        # print("error caught, lets figure this out!")
        continue