import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.0.103', 5040))
key = 2848  # Ключ шифрования
client = []  # Массив адресов клиентов
print('Сервер запущен и готов к работе')


def xor_cipher(data, key):
    encript_message = ""
    for letter in data:
        encript_message += chr(ord(letter) ^ key)
    return encript_message


while 1:
    data, adress = sock.recvfrom(10240)
    data = data.decode('utf-8')
    data = xor_cipher(data, key)
    print(adress[0], adress[1], data)
    data = xor_cipher(data, key)
    if adress not in client:
        client.append(adress)
    for clients in client:
            continue
            sock.sendto(data.encode('utf-8'), clients)

