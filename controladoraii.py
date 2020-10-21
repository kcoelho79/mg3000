import socket
import BitHandler as convert



def serializa_frame(frame):
    print("FRAME :",frame)

    frame_evento = {}

    cabecalho = frame[0:2]
    comando = frame[5:6]
    tamanho_bytes_msg = frame[3] + frame[4]
    print(tamanho_bytes_msg)
    frame_evento = get_frame_evento(frame[5:],tamanho_bytes_msg)
    print(convert.Byte_to_Hex(frame_evento))




def get_frame_evento(msg,tamanho):
    frame_evento = msg[:21]  #pega msg
    frame_evento = frame_evento[2:] # retira rodape
    return frame_evento

def evento(msg):
    pass


def checksum(frameHex):
    # receber array inteiro
    # fazer as somas byte a byte valor inteiro
    # converter inteiro para hex int.to_byte(2,'little')
    # pegar resultado[0]

    cs = 0
    msg = frameHex[3:]
    for i in range(len(msg)):
        print("framehex :",frameHex[i])
        cs += frameHex[i]
        print("cs: ",cs)
    cs = hex(cs)
    print("tamanho",len(cs))
    return cs


#--- Ler Data e Hora
def opcao12(data):

    print ("received data:", data)
    print("tamanho do retorno data: ", len(data))
    print("tipo do dado recebido: ", type(data))
    print("------------------------------------")
    print("pos0: ",data[0])
    print("pos1: ",data[1])
    print("dia: ",data[2])
    print("mes: ",convert.bcd2int(data[3]))
    print("ano: ",convert.bcd2int(data[4]))
    print("hora: ",convert.bcd2int(data[5]))
    print("min: ",convert.bcd2int(data[6]))
    print("seg: ",convert.bcd2int(data[7]))
    print("cs: ",data[8])
    print("data: "+ str(convert.bcd2int(data[2])) +"/" + str(convert.bcd2int(data[3])) +"/"+ str(convert.bcd2int(data[4]))+" "+str(convert.bcd2int(data[5]))+":"+str(convert.bcd2int(data[6])))

#  MAIN ()

# Conexao TCP

def enviarComando(comando):

    #FrameHex = bytearray(comando)
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

def parse_dados(dados):
    print(dados.fromhex)
    for i in range(len(dados)):
        print(f"byte {i} = inteiro:{dados[i]}  hex: {hex(dados[i])} bcd: {convert.bcd2int(dados[i])}")


