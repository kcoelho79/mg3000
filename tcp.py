import socket


def bcd2int(bcd):
    digit=0
    ret=0

    digit = (bcd >> 4) & 0x0F
    ret = ret * 10 + digit;

    digit = bcd & 0x0F
    ret = ret * 10 + digit
    return ret


#--- opcao 12
def opcao12(data):

    print ("received data:", data)
    print("tamanho do retorno data: ", len(data))
    print("tipo do dado recebido: ", type(data))
    print("------------------------------------")
    print("pos0: ",data[0])
    print("pos1: ",data[1])
    print("dia: ",data[2])
    print("mes: ",bcd2int(data[3]))
    print("ano: ",bcd2int(data[4]))
    print("hora: ",bcd2int(data[5]))
    print("min: ",bcd2int(data[6]))
    print("seg: ",bcd2int(data[7]))
    print("cs: ",data[8])
    print("data: "+ str(bcd2int(data[2])) +"/" + str(bcd2int(data[3])) +"/"+ str(bcd2int(data[4]))+" "+str(bcd2int(data[5]))+":"+str(bcd2int(data[6])))

#  MAIN ()

# Conexao TCP

#TCP_IP = '10.238.10.108'
TCP_IP = '10.238.0.41'

TCP_PORT = 9000 #9762
BUFFER_SIZE = 1024
MESSAGE = bytearray(b'\x00\x0C\x0C')
print("soma checksum: ",sum(MESSAGE[:-1]))
tamFrame = (len(MESSAGE))
print("Tamanho do frame: ",tamFrame)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)

# --- Retorno

data = s.recv(BUFFER_SIZE)
s.close()

# - ler data e hora

opcao12(data)
