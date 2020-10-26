import BitHandler as convert

# open connect to controllerII
#import server

# abre conexao
# recebe comando
#

data = b'STX\x00\x15\x00t\x00(\x11\x00\x03\x00\x00F\x89\n\t\x13\x06\x02\x01\x00\x00T\x02ETX'

def recebeMensagem(fbytes):
    #particiona fbytes
    cabecalho = fbytes[0:2]
    comando = fbytes[5:6]
    tamanho_fbytes_msg = fbytes[3] + fbytes[4]
    # convert.Byte_to_Hex(payload)
    return payload
    

def evento(frame):

    # estrutuda de dados
    frameEvt = frame[9:-3]
    msgEvt = {
        'tipo_evt'              : tipoEvento(frameEvt[0]),
        'setor'                 : setor(frameEvt[0]),
        'modo_operacao'         : modeOperacao(frameEvt[1]),
        'numero_dispositivo'    : numeroDispositivo(frameEvt[1]),
        't_disp_Anviz'          : tDispAnviz(frameEvt[2]),
        'tipo_dispositivo'      : tipoDispositivo(frameEvt[2]),
        'numero_serial'         : numeroSerial(frameEvt[3:7+1]),
        'hora_data'             : horaData(frameEvt[8:13+1]),
        'nivel'                 : nivel(frameEvt[14]),
        'bateria'               : bateria(frameEvt[15]),
        'leitora_acionada'      : leitoraAcionada(frameEvt[15]),        
        'flag_evento'           : flagEvento(frameEvt[15])
    }

    return msgEvt

def leitoraAcionada(byte):
    leitora = convert.bits2int(byte,1,2) # bit1:2

    lista_leitora = [
        'leitora Acionada 01',
        'leitora Acionada 02',
        'leitora Acionada 03',
        'leitora Acionada 04'
    ]

    return lista_leitora[leitora]    


def bateria(byte):
    bateria = convert.onebit(byte,0)
    print("BATERIA ====",bateria)
    if bateria == 0:
        return 'bateria OK'
    else:
        return 'bateria fraca'


def flagEvento(byte):   
    pass
    #infoEvento = convert.bits2int(byte,4,7)

        
def nivel(byte):
    pass

def horaData(byte):

    print("tamanho",len(byte))
    print(convert.fmtByte_to_Str(byte))
    hora        = byte[0]
    minuto      = byte[1]
    segundo     = byte[2]
    dia         = byte[3]
    mes         = byte[4]
    ano         = byte[5]

    return (
        "data: "+ 
        str(convert.bcd2int(dia)) + "/" + 
        str(convert.bcd2int(mes)) +"/"+ 
        str(convert.bcd2int(ano))+" "+
        str(convert.bcd2int(hora))+":"+
        str(convert.bcd2int(minuto))
    )




def numeroSerial(byte):
    return convert.fmtByte_to_Str(byte)   
    #return byte     

def tipoDispositivo(byte):
    mask = 0x0F
    valor = (byte & mask)

    lista_tipo_dispositivo = [
         '--> SEM USO',
         '--> DISP_TX',
         '--> DISP_TA', 
         '--> DISP_CT',
         '--> DISP_CA',
         '--> DISP_BM',
         '--> DISP_TP',
         '--> DISP_SN',
         '--> SEM USO', 
         '--> SEM USO', 
         '--> SEM USO',
         '--> DISP_CM', 
         '--> SEM USO',
         '--> SEM USO',
         '--> DISP_APAGADO', 
         '--> DISP_VAGO'

    ]

    return lista_tipo_dispositivo[valor]

def tDispAnviz(byte):
    mask = 0xF0 # bits Alta 11110000
    valor = (byte & mask)

    if valor == 3:
        return "CARTAO"
    elif valor == 5:
        return "BIOMETRIA"
    elif valor == 7:
        return "SENHA"
    else:
        return "NAO IMPLEMENTADO"

def numeroDispositivo(byte):
    #bits5:0
    valor = convert.bits2int(byte, 5, 0)
    return valor

def modeOperacao(byte):
    # bits6:7 ordem little
    valor = convert.bits2int(byte, 6, 7)

    lista_modo_operacao= [
        'MODO CATRACA',
        'MODO PORTA',
        'MODO CANCELA'
    ]
   
    return lista_modo_operacao[valor]


def tipoEvento(byte):
    #aplica mask 0001111 (0x1f), range bit4:bit0
    valor = (byte & 0x1f)
           
    lista_tipo_eventos= [
            'dispositivo acionado',
            'Passagem',
            'Equipamento Ligado',
            'Habilitacao sem vagas',
            'Mudanca de programacao',
            'Acionamento Remoto Concetrador',
            'Acionamento remoto PC',
            'Contador de Atualizaçao',
            'Tentativa de clonagem',
            'Evento de Panico',
            'SDCARD Removido',
            'Restore Efetuado',
            'Erro de gravacao',
            'Backup Automatico',
            'Backup Manual',
            'Nao Cadastrado',
            'Dupla Passagem',
            'Nao Habilitado',
            'BootLoader',
            'Alarme Entrada Digital',
            'Reset WatchDog',
            'Atualizado'

        ]

    return lista_tipo_eventos[valor]

def setor(byte):
    # aplica mask 1110000 (0xE0), range bit7:bit5
    valor = byte & 0xE0

    return valor        




    # partciona frame, pega o frame de evento
    print("INICIO funcao EVENTO")
    fbytes = fbytes[9:-3]
    print(fbytes[0])
    fevento = {
        'tipo_evento': lista_tipo_eventos[int(convert.tobit(fbytes[0], 4, 0), 2)]
    }

    

    
    print("FIM funcao EVENTO")
    return fevento


print('-----')
print('imprinmi data original :', data)
#data=recebeMensagem(data)
print("data transformadao payload ...", data)
print(evento(data))