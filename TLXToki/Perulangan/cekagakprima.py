import math
x = int(input())
hasil = 0
for i in range(1, x+1):
    n = int(input())
    if n <= 11:
        print("YA")
        i += 1
        continue
    j = 2
    while j*j <=n:
        if n % j == 0:
            if n / j == j:
                hasil += 1
            else:
                hasil += 2
        if hasil == 3:
            break
        
        j += 1
    if hasil < 3:
        print("YA")
    else:
        print("BUKAN")
    hasil = 0
    i += 1