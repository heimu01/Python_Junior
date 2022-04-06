import socket

sock = socket.socket()
sock.connect(('0.tcp.ngrok.io', 14785))

while True:
    sock.send(str.encode(input('mess: ')))
    data = sock.recv(1024)
    print(bytes.decode(data))

sock.close()

