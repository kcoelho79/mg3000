
import BitHandler as convert
import enviar as server
# GravarDispositivo comando80 0x0050

#estrutura de dados

def msgRetorno(b):
    lista = [
        'OK (Sucesso)',
        'memoria cheia',
        'dispositivo cadastrado',
        'sem mais eventos',
        'fim do arquivo',
        'estouro do buffer interno',
        'conflito de portas',
        'erro no tamanho do pacote',
        'erro de checksum',
        'erro modo de operaçao',
        'erro escrita/leitura',
        'erro fora do limite do dispositivo',
        'erro tipo diferente',
        'erro operacao invalida',
        'erro dispositivo diferente',
        'erro indice invalido',
        'erro de sintaxe',
        'erro valor invalidado',
        'erro serial invalido',
        'erro setor diferente',
        'erro endereço diferente',
        'erro biometria 1 sucesso biometria 2',
        'erro biometria 2 sucesso biometria 1',
        'erro biometria 1 e 2'
    ]

    return lista[b]

#comando 0x0075 Acionamento
def acionamento(dispositivo,endplaca,saida):
    print('comando Acionamento')

    payload = bytearray()
    comando = b'\x00\x75'

    payload.extend(comando)
    payload.append(dispositivo)
    payload.append(endplaca)
    payload.append(saida)
    cs = convert.calcula_checksum(payload)
    payload.append(cs)

    bretorno = server.enviarComando(payload)

    print(msgRetorno(bretorno[7]))
    return msgRetorno(bretorno[7])


def acionamentoIdentificacao(dispositivo,endplaca,saida,serial):
    print('comando Acionamento com Identificação')

    payload = bytearray()
    comando = b'\x00\x84'

    payload.extend(comando)
    payload.append(dispositivo)
    payload.append(endplaca)
    payload.append(saida)

    #tipo dispositivo
    payload.append(3)

    # byte serial
    payload.append(0)
    payload.extend(bytearray.fromhex(serial))

    # Byte flagsCadastro
    payload.append(0)

    # Byte  nivel
    payload.append(1)

    # Byte origemAcionamento
    payload.append(1)

    # Byte Checksum
    cs = convert.calcula_checksum(payload)
    payload.append(cs)

    bretorno = server.enviarComando(payload)

    print('RETORNO COMANDO 132 :',bretorno)

def gravarDispositivo(serial,usuario,visitante= False):

    payload  = bytearray()
    #tamanho
    # payload += b'\x00\x24'
    #comando
    payload += b'\x00\x50'


    # FRAME DISPOSITIVO

    # byte 1 tipoDispositivo
    payload.append(3)

    # bytes 2-6 serial
    s1, s2 = serial.split('-')          # separa o prefixo 2 algarismo e o  sufixo 4 algarismo do serial
    s1 = int(s1).to_bytes(1, 'big')     #converte inteiro para byte
    s2 = int(s2).to_bytes(2, 'big')
    #serial = bytes.fromhex('00') +s1 + s2                    # concatena o prefixo e sufixo do serial, bytes
    serial = b'\x00\x00\x00' +s1 +s2
    print(serial.hex())
    payload.extend(serial)

    # Byte 7 codHAB(High)
    payload.append(0)

    # Byte 8 codHAB(Low)
    payload.append(0)

    # Byte 9 flagsCadastro
    if visitante:
        payload.append(3)
    else:
        payload.append(0)


    # Byte 10 flagsStatus
    payload.append(16)

    # Byte 11 nivel
    payload.append(255)

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

    for i in range(tamanho_frame - len(usuario)):
        usuario += b'\x00'


    payload.extend(usuario)

    # calcula checksum
    cs = convert.calcula_checksum(payload)

    payload.append(cs)

    server.enviarComando(payload)


#gravarDispositivo('070-35082','KLEBER84',visitante = True )
# print( convert.fmtByte_to_Str(acionamento(0,9,3),separador=' '))

#fazer
#trocar append por  == lista
#verificar o len do serial, acescentar zero
#testar
