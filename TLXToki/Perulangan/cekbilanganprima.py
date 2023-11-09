import math
x = int(input())

for i in range(1, x+1):
    n = int(input())
    hasil = 0
    for j in range(2, math.isqrt(n)+1):
        if n % j == 0:
            hasil += 1
    if n == 1:
        print("BUKAN")
    elif hasil >= 1:
        print("BUKAN")
    else:
        print("YA")
            
    