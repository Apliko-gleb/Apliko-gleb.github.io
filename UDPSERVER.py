import socket
import time

# Устанавливаем адрес и порт сервера
host = socket.gethostname()     # Получить имя локальной машины.
server_address = (host, 5000)
# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Привязываем сокет к заданному адресу и порту
server_socket.bind(server_address)
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   
print("Your Computer Name is:"+hostname)   
print("Your Computer IP Address is:"+IPAddr) 
while True:
    # Ждем получение данных от клиента
    data, client_address = server_socket.recvfrom(1024)
    # Засекаем время приема данных
    receive_time = time.time()

    # Отправляем обратно клиенту ответное сообщение
    server_socket.sendto(b"Received", client_address)

    # Рассчитываем задержку
    delay = receive_time - float(data)

    print(f"Received message from {client_address}, Delay: {delay} seconds")