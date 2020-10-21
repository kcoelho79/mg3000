def bit_from_string(string, index, msb= False ):
       i, j = divmod(index, 8)
      # print(i,j)

       # msb (most significant bit) if true set the high-order bit first
       if msb:
           j = 8 - j

       if ord(string[i]) & (1 << j):
              return 1
       else:
              return 0

def Byte_to_Hex(frame):
    tamanho = len(frame)
    frameHex= []
    for i in range(tamanho):
        frameHex.append(hex(frame[i]))
    return frameHex


def Hex_to_Bin(hexnumber, num_of_bits=8):
    base=16
    return bin(int(hexnumber,base))[2:].zfill(num_of_bits)

def bcd2int(bcd):
    digit=0
    ret=0

    digit = (bcd >> 4) & 0x0F
    ret = ret * 10 + digit;

    digit = bcd & 0x0F
    ret = ret * 10 + digit
    return ret



