import socket
import threading


def xor_cipher(message, key):
    encript_message = ""
    for letter in message:
        encript_message += chr(ord(letter) ^ key)
    return encript_message


def read_sok():
    while 1:
        data = soc.recv(10240)
        data = data.decode('utf-8')
        data = xor_cipher(data, key)
        print(data)


server = '192.168.0.103', 5040  # Данные сервера
key = 2848  # Ключ шифрования
print('Введите свой никнейм:')
nickname = input()  # Никнейм для общения
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind(('', 0))  # Задаем сокет как клиент
soc.sendto(xor_cipher((nickname + ' подключился к чату'), key).encode('utf-8'), server)  # Уведомляем чат о подключении
thread = threading.Thread(target=read_sok)
thread.start()
while 1:
    message = input()
    cripted_message = xor_cipher('[' + nickname + '] ' + message, key)
    soc.sendto(cripted_message.encode('utf-8'), server)