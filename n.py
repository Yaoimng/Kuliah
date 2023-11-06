a = int(input())
b = int(input())

if a % 2 == 0:
    a+=1
if b % 2 == 0:
    b-=1
n = (b-a)//2+1
hasil = int(n*(a+b)/2)
print(hasil)