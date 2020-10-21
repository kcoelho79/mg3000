import socket


def bcd2int(bcd):
    digit=0
    ret=0

    digit = (bcd >> 4) & 0x0F
    ret = ret * 10 + digit;

    digit = bcd & 0x0F
    ret = ret * 10 + digit
    return ret

def checksum(frameHex):
    tamFrameHex = len(frameHex)
    frameEnvioHex = frameHex
    frameHex.append(0)


    for i in range(tamFrameHex):
        print(i)
        frameEnvioHex[tamFrameHex] += frameHex[i]


    return frameEnvioHex[tamFrameHex]


#--- Ler Data e Hora
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

def enviarComando(comando):
    FrameHex = bytearray(comando)
    print("soma checksum: ",sum(comando[:-1]))
    tamFrame = (len(comando))
    print("Tamanho do frame: ",tamFrame)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(comando)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print(len(data))
    print(data)
    return data


#cTCP_IP = '10.238.10.109'
TCP_IP = '10.238.0.41'

TCP_PORT = 9000 #9762
BUFFER_SIZE = 1024
#MESSAGE = bytearray(b'\x00\x0C\x0C')


# --- Retorno
retorno = enviarComando(b'\x53\x54\x58\x00\x03\x00\x5f\x5f\x45\x54\x58')
#enviarComando(b'\x00\x03\x03')
print ("retorno : ")
print(retorno[2])


#opcao12(retorno)
