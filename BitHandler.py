def bit_from_string(string, index, msb= False ):
       i, j = divmod(index, 8)

       # msb (most significant bit) if true set the high-order bit first
       if msb:
           j = 8 - j

       if ord(string[i]) & (1 << j):
              return 1
       else:
              return 0

b = b"kleber"
s = b.decode(" utf-8")

for i in range(8):
    print("lsb :",i, bit_from_string(s,i))
    print("MSB :",i, bit_from_string(s,i,msb= True ))
