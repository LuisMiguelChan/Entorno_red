import socket
from typing import NoReturn

socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Nos conectamos a la dirección y puerto del server
host = "127.0.0.1"
port = 8001
socket_client.connect((host,port))
seguir = True
while seguir == True:
    entrada = True
    print("Ingrese un mensaje para el servidor")
    mensaje = input("Cliente: ")
    socket_client.send(mensaje.encode('utf-8'))

    while entrada == True:    
        respuesta = socket_client.recv(1024) #este método debe ser indicado en bytes
        respuesta = respuesta.decode('utf-8')
        print(f"Server: {respuesta}")

        if respuesta==".":
            print("Enviar otro mensaje [si][no]")
            espera=input("Cliente: ")

            if espera=="si":
                seguir=True
                entrada=False
            else:
                seguir=False
                entrada=False
