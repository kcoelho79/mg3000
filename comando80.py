
import BitHandler as convert
import enviar as server
# GravarDispositivo comando80 0x0050

#estrutura de dados


def gravarDispositivo(serial,usuario):

    payload  = bytearray()
    #tamanho
    payload += b'\x00\x24'
    #comando
    payload += b'\x00\x50'


    # FRAME DISPOSITIVO

    # byte 1 tipoDispositivo
    payload.append(3)

    # bytes 2-6 serial
    s1, s2 = serial.split('-')          # separa o prefixo 2 algarismo e o  sufixo 4 algarismo do serial
    s1 = int(s1).to_bytes(1, 'big')     #converte inteiro para byte
    s2 = int(s2).to_bytes(2, 'big')
    serial = bytes.fromhex('00') +s1 + s2                    # concatena o prefixo e sufixo do serial, bytes
    serial = b'\x00\x00\x00' +s1 +s2
    print(serial.hex())
    payload.extend(serial)

    print(payload)

    # Byte 7 codHAB(High)
    payload.append(0)

    # Byte 8 codHAB(Low)
    payload.append(0)

    # Byte 9 flagsCadastro
    payload.append(0)

    # Byte 10 flagsStatus
    payload.append(16)

    # Byte 11 nivel
    payload.append(2)

    # Byte 12 creditos
    payload.append(255)


    # Byte 13 a 18 Validade data incio e fim
    payload.append(1)    # inicio dia 01
    payload.append(1)    # inicio mes 01
    payload.append(20)   # inicio ano 2020
    payload.append(20)   # fim dia 20
    payload.append(12)  # fim mes 12
    payload.append(30)   # fim ano 2040


    # Byte 19 a 31 Identidicacao do usuario
    tamanho_frame = 14
    usuario = str.encode(usuario) # converte str para bytes

    # preenhe o restante com 0x20 até o total do tamFrame
    for i in range(tamanho_frame - len(usuario)):
        usuario = usuario + usuario.fromhex('20')

    print(usuario)

    payload.extend(usuario)

    # calcula checksum
    print("Checksum -----")
    range_cs = payload[2:]
    print(convert.fmtByte_to_Str(range_cs))
    cs = 0
    for i in range(len(range_cs)):
        cs = cs + range_cs[i]
        print("posicao %i HEX %s soma= %i " %(i, hex(range_cs[i]), cs))

    print("CS TOTAL =>",hex(cs))

    cs = cs & 0xff0 >> 4

    payload.append(cs)

    print("ANTES DE DE ENVIAR -=----")
    print(len(payload))

    server.enviarComando(payload)



gravarDispositivo('070-35082','TESTE1')

#fazer
#trocar append por  == lista
#verificar o len do serial, acescentar zero
#testar



