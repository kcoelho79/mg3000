import socket


def bcd2int(bcd):
    digit=0
    ret=0

    digit = (bcd >> 4) & 0x0F
    ret = ret * 10 + digit;

    digit = bcd & 0x0F
    ret = ret * 10 + digit
    return ret

TCP_IP = '192.168.1.12'
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

def checksum(frameHex):
    tamFrameHex = len(frameHex)
    frameEnvioHex = frameHex
    frameHex.append(0)


    for i in range(tamFrameHex):
        print(i)
        frameEnvioHex[tamFrameHex] += frameHex[i]


    return frameEnvioHex[tamFrameHex]

MESSAGE = bytearray(b'\x00\x0C')
print(enviaComando(MESSAGE))
return frameEnvioHex



