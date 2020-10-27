
import BitHandler as convert
# GravarDispositivo comando80 0x0050

#estrutura de dados

def wegand2serial(num):
    W1,W2 = num.split('-')
    W1 = int(W1).to_bytes(1,'big')
    W2 = int(W2).to_bytes(2,'big')
    serial = W1 + W2
    print(serial.hex())
    return serial


def id_Usuario():

    id_usuario = input("Entre com a identificacao usuario :")
    id_usuario_as_byte = bytearray(0)
    for i in range(len(id_usuario)-1):
        id_usuario_as_byte.append(ord(id_usuario[i]))
    p = 14 - len(id_usuario)

    id_usuario_as_byte = id_usuario_as_byte + (ord('k') * p)
    print(id_usuario_as_byte)
    print(len(id_usuario_as_byte))


comando             = (b'/x00/x50')
tipoDisp            = (b'/x03')
serial              = wegand2serial('015-02158')
codHabH             = (b'/x00')
codHabL             = (b'/x00')
flagCadastro        = (b'/x06')
flagStatus          = (b'/x10')
nivel               = (b'/x02')
credito             = (b'/xff')
val_dia_ini         = (b'/x01') #  inicio dia 01
val_mes_ini         = (b'/x01') #  inicio mes 01
val_ano_ini         = (b'/x14') #  inciio ano 2020
val_dia_fim         = (b'/x14') #  ate dia 20
val_mes_fim         = (b'/x0c') #  ate mes 12
val_ano_fim         = (b'/x28') #  ate ano 2040
userLabel           = id_Usuario()

wegand2serial('015-02158')
wegand2serial('070-35082')

#formatar msg hexadecimal

#enviar

