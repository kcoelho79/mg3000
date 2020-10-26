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
        'evento_lido'           : eventoLido(frameEvt[15]),       
        'info_evento'           : infoEvento(frameEvt[15],frameEvt[0])
    }

    return msgEvt

def infoEvento(b_info_evt,b_tipo_evt):
    valor_evento = (b_tipo_evt & 0x1f)
    valor_info_evento = convert.bits2int(b_info_evt,4,7)

             
    lista_tipo_eventos= [
           [
                'SUB_LOG_ACIONAMENTO_ENTRADA',
                'SUB_LOG_ACIONAMENTO_SAIDA',
                'SUB_LOG_ACIONAMENTO_BOTAO_1',
                'SUB_LOG_ACIONAMENTO_BOTAO_2',
                'SUB_LOG_ACIONAMENTO_BOTAO_3',
                'SUB_LOG_ACIONAMENTO_BOTAO_4',
                'SUB_LOG_AGUARDANDO_SEGUNDA_VALIDACAO'],
           [
                'SUB_LOG_PASSAGEM_ENTRADA_1',
                'SUB_LOG_PASSAGEM_SAIDA_1',
                'SUB_LOG_PASSAGEM_ENTRADA_2',
                'SUB_LOG_PASSAGEM_SAIDA_2',
                'SUB_LOG_PASSAGEM_ENTRADA_3',
                'SUB_LOG_PASSAGEM_SAIDA_3',
                'SUB_LOG_PASSAGEM_ENTRADA_4',
                'SUB_LOG_PASSAGEM_SAIDA_4',
                'SUB_LOG_PASSAGEM_TOUT',
                'SUB_LOG_PASSAGEM_SAIDA_LIVRE',
                'SUB_LOG_PASSAGEM_BOTAO_1',
                'SUB_LOG_PASSAGEM_BOTAO_2',
                'SUB_LOG_PASSAGEM_BOTAO_3',
                'SUB_LOG_PASSAGEM_BOTAO_4',
                'SUB_LOG_PASSAGEM_ENTRADA_APB_DESLIGADO',
                'SUB_LOG_PASSAGEM_SAIDA_APB_DESLIGADO'
                ],

           [    '2 SEM USO'],

           [    'SUB_LOG_HABILITACAO_SEM_VAGAS'],

           [    '4 SEM USO'],

           [
                'SUB_LOG_ACIONAMENTO_REMOTO_OK',
                'SUB_LOG_ACIONAMENTO_REMOTO_ERRO',
                'SUB_LOG_ACIONAMENTO_REMOTO_COM_ID_OK',
                'SUB_LOG_ACIONAMENTO_REMOTO_COM_ID_ERRO',
                'SUB_LOG_ACIONAMENTO_REMOTO_RELE_5',
                'SUB_LOG_ACIONAMENTO_REMOTO_RELE_6'
                ],

           [
                'SUB_LOG_ACIONAMENTO_REMOTO_OK',
                'SUB_LOG_ACIONAMENTO_REMOTO_ERRO',
                'SUB_LOG_ACIONAMENTO_REMOTO_COM_ID_OK',
                'SUB_LOG_ACIONAMENTO_REMOTO_COM_ID_ERRO',
                ],

            [   'SUB_LOG_INCONSISTENCIA_ENTRE_BASES_DE_DADOS'],

            [   '8 SEM USO'],

            [
                'SUB_LOG_PANICO',
                'SUB_LOG_PANICO_NAO_ATENDIDO',
                'SUB_LOG_PANICO_CANCELADO',
                'SUB_LOG_PANICO_2X_CARTAO',
                'SUB_LOG_PANICO_IMEDIATO',
                'SUB_LOG_PANICO_TEMPORIZADO',
                'SUB_LOG_PANICO_DISPOSITIVO'
                ],

            [   '10 SEM USO'],

            [   '11 SEM USO'],

            [
                'SUB_LOG_ERRO_GRAVAÇÃO_BIOMETRIA_1',
                'SUB_LOG_ERRO_GRAVAÇÃO_BIOMETRIA_2',
                'SUB_LOG_ERRO_GRAVAÇÃO_BIOMETRIA_3',
                'SUB_LOG_ERRO_GRAVAÇÃO_BIOMETRIA_4',
                'SUB_LOG_ATUALIZAÇÃO_CANCELADA_ERROS'
                ],

            [   '13 SEM USO'],

            [   '14 SEM USO'],

            [
                'SUB_LOG_NAO_CADASTRADO',
                'SUB_LOG_LEITORA_EXPEDIDORA'],

            [
                'SUB_LOG_DUPLA_PASSAGEM_ENTRADA_1',
                'SUB_LOG_DUPLA_PASSAGEM_SAIDA_1',
                'SUB_LOG_DUPLA_PASSAGEM_ENTRADA_2',
                'SUB_LOG_DUPLA_PASSAGEM_SAIDA_2',
                'SUB_LOG_DUPLA_PASSAGEM_ENTRADA_3',
                'SUB_LOG_DUPLA_PASSAGEM_SAIDA_3',
                'SUB_LOG_DUPLA_PASSAGEM_ENTRADA_4',
                'SUB_LOG_DUPLA_PASSAGEM_SAIDA_4'],

            [
                '0=VALIDO',
                '1=INVALIDO_NAO_CADASTRADO',
                '2=INVALIDO_LEITORA_COFRE',
                '3=INVALIDO_ANTI_PASSBACK',
                '4=INVALIDO_SEM_CREDITOS',
                '5=INVALIDO_DATA_VALIDADE_EXPIRADA',
                '6=INVALIDO_TEMPO_ANTICARONA',
                '7=INVALIDO_LEITORA_NAO_HABILITADA',
                '8=INVALIDO_FERIADO',
                '9=INVALIDO_JORNADA_TURNO',
                '10=INVALIDO_SEM_VAGAS_NIVEL',
                '11=INVALIDO_LEITORA_INIBIDA'
                ],

            [   '18 SEM USO'],

            [
                'SUB_LOG_ALARME_ED_1',
                'SUB_LOG_ALARME_ED_2',
                'SUB_LOG_ALARME_ED_3',
                'SUB_LOG_ALARME_ED_4',
                'SUB_LOG_ARROMBAMENTO1',
                'SUB_LOG_ARROMBAMENTO2',
                'SUB_LOG_ARROMBAMENTO3',
                'SUB_LOG_ARROMBAMENTO4'],

            
            [   '20 SEM USO'],

            [
                'SUB_LOG_ATUALIZACAO_FALHA_DE_GRAVACAO',
                'SUB_LOG_ATUALIZACAO_CONCLUIDA_COM_SUCESSO',
                'SUB_LOG_ATUALIZACAO_SERIAL_FORA_DO_LIMITE'

            ]

        ]
    return lista_tipo_eventos[valor_evento][valor_info_evento]

def eventoLido(byte):
    if conver.onebit(byte,3) == 0:
        return 'Comando ainda nao lido por comando PC'
    else:
        return 'evento já lido através de comando PC'

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