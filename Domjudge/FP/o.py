def panjangstr(n):
    return len(str(n))

def terbesar(x, y):
    while y:
        x, y = y, x % y
    return x

def bukabrankas(x, y):
    greatest = terbesar(x, y)
    total = panjangstr(greatest)
    
    return total % 2 == 0

input_data = input().split()
x, y = map(int, input_data)

if bukabrankas(x, y):
    print("Yey brankas berhasil dibuka :D")
else:
    print("Yah gagal :(")
