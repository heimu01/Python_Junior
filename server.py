import socket

sock = socket.socket()
sock.bind(('', 5000))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    conn.send(data.upper())

    conn.close()