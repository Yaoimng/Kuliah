def stringtobinary(n):
    binary_list = []
    for char in n:
        binary_list.append(bin(ord(char))[2:].zfill(8))
    return ''.join(binary_list)

def binarytostring(binary_str):
  byte_list = []
  for i in range(0, len(binary_str), 8):
    byte = int(binary_str[i:i+8], 2)
    byte_list.append(chr(byte))
  return ''.join(byte_list)


x = int(input())
input = input()

if x == 1:
    hasil = stringtobinary(input)
    print (hasil)
elif x == -1:
    hasil = binarytostring(input)
    print (hasil)