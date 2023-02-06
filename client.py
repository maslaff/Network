import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 55555  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        mesg = input('>>>')
        if mesg.lower() == 'exit':
            break
        s.sendall(mesg.encode())
        data = s.recv(1024)
        if data:
            print(data)

print(f"Received {data!r}")
