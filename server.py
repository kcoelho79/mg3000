import socket
import controladoraii as Controler
import orchestrator

TCP_IP = '10.238.10.103'
TCP_PORT = 9767
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind((TCP_IP, TCP_PORT))
serv_socket.listen(1)
print( "aguardando conexao")
conn, addr = serv_socket.accept()
print ("Connection address:", addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: 
        break
    print ("received data:", data)
    #Controler.serializa_frame(data)
    orchestrator.evento(data)

    #conn.send(data)  # echo
conn.close()
