import socket
import re

#AF_INET se refiere a una familia IP
#SOCK_STREAM indica que es una conexión TCP
socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Especificamos la dirección ip y el puerto en el cual
#escuchará nuestro servidor
ip = "127.0.0.1"
port = 8001
socket_server.bind((ip,port))
socket_server.listen(15) #Máximo de conexiones

patron1 = r"[aeiouAEIOU]"
patron2 = r"[a-zA-Z]{1,}\b"
patron3 = r"[0-9]"
patron4 = r"[A-Z]\w+"
patron5 = r"[a-zA-Záéíóú]{1,}[^aeiouAEIOUáéíóú\s\W]\b"

print(f"\n\nServidor en espera direccion {ip}:{port}")

while True:
    conexion, address = socket_server.accept()
    print ("La conexión  ha sido establecida")
    
    while True:
        
        message = conexion.recv(1024)
        message = message.decode()
        print(message)

        coincidencias = re.findall(patron1, message)
        suma = 0
        for coincidencia in coincidencias:
            suma=suma+1
            print(coincidencia)

        mensaje = f"Se encontraron {suma} vocales"
        conexion.send(mensaje.encode('utf-8'))

        coincidencias = re.findall(patron2, message)
        suma = 0
        for coincidencia in coincidencias:
            suma=suma+1
            print(coincidencia)
        
        mensaje = f"Se encontraron {suma} palabras"
        conexion.send(mensaje.encode('utf-8'))

        coincidencias = re.findall(patron3, message)
        suma = 0
        for coincidencia in coincidencias:
            suma=suma+1
            print(coincidencia)

        mensaje = f"Se encontraron {suma} numeros"
        conexion.send(mensaje.encode('utf-8'))

        coincidencias = re.findall(patron4, message)
        suma = 0
        for coincidencia in coincidencias:
            suma=suma+1
            print(coincidencia)

        mensaje = f"Se encontraron {suma} palabras que inician con una letra mayuscula"
        conexion.send(mensaje.encode('utf-8'))
        
        coincidencias = re.findall(patron5, message)
        suma = 0
        for coincidencia in coincidencias:
            suma=suma+1
            print(coincidencia)

        mensaje = f"Se encontraron {suma} palabras que no finalizan con una vocal"
        conexion.send(mensaje.encode('utf-8'))

        mensaje = "."
        conexion.send(mensaje.encode('utf-8'))