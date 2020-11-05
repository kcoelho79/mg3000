import socket
import BitHandler as convert


def enviarComando(payload):
    cabecalho = b'STX'
    rodape = b'ETX'
    tamanho = int.to_bytes(len(payload),2,'big')
    frame = cabecalho + tamanho + payload +rodape

    # add cabecalho + payload = com isso faco a soma do checksum, add checksum + rodape

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    print("ENVIANDO HEX  :", convert.fmtByte_to_Str(frame,separador=' '))
    s.send(frame)
    data = s.recv(BUFFER_SIZE)
    s.close()
    #Verifica se retorno comando 80 e retorno = ok

    # print("data  retorno :", convert.fmtByte_to_Str(data,separador=' '))

    return data



TCP_IP = '10.238.10.111'
#TCP_IP = '10.238.0.41'

TCP_PORT = 9762
BUFFER_SIZE = 1024

