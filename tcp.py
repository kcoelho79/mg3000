import socket


TCP_IP = '10.238.10.108'
TCP_PORT = 9000 #9762
BUFFER_SIZE = 1024
MESSAGE = bytearray(b'\x00\x0C\x0C')
print("soma checksum: ",sum(MESSAGE[:-1]))
tamFrame = (len(MESSAGE))
print("Tamanho do frame: ",tamFrame)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)

data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)
print("tamanho do retorno data: ", len(data))
print("tipo do dado recebido: ", type(data))
print("------------------------------------")
print("pos0: ",data[0])
print("pos1: ",data[1])
print("dia: ",data[2])
print("mes: ",data[3])
print("ano: ",data[4])
print("hora: ",data[5])
print("min: ",data[6])
print("seg: ",data[7])
print("cs: ",data[8])
