import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "айпи сервера"
PORT = 12333
connection.connect((IP, PORT))
rd = connection.recv(1024)
print(rd.decode('utf8'))
connection.send("И тебе привет!".encode('utf8'))
connection.close()