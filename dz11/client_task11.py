import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
message1 = input("Espresso or Cappuccino? ")
sock.send(bytes(message1, encoding='UTF-8'))
data = sock.recv(1024)
print(data)
message2 = input("And for your partner? ")
sock.send(bytes(message2, encoding='UTF-8'))
data = sock.recv(1024)
print(data)
sock.close()