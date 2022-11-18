import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Server is ok, nnnnnice')
total = []
while True:
    conn, addr = sock.accept()
    print('connected', addr)
    menu = {bytes('Espresso', encoding='UTF-8') : '1', bytes('Cappuccino', encoding='UTF-8'): '2'}
    data1 = conn.recv(1024)
    try:
        print(menu[data1])
        answer = "That will cost you " + menu[data1] + "$"
        conn.send(bytes(answer, encoding='UTF-8'))
        data2 = conn.recv(1024)
    except KeyError as ex:
        conn.send(bytes('naaaaah', encoding='UTF-8'))
    total = int(menu[data1]) + int(menu[data2])
    print(total)
    conn.send(bytes("Total price of your order is " + str(total)+ " American Dollars", encoding='UTF-8'))
conn.close()