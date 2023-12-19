tempat = [-1 for x in range(39)]
tempat[0] = 9
tempat[1] = 10
tempat[2] = 20

x = [0 for x in range(43)]
x[2] = 1
x[3] = 0
x[4] = -1
x[5] = -2
for i in range(6,43):
    x[i] = x[i-1] - 1
def fib(n):
    if(tempat[n] != -1):
        return tempat[n]
    else:
        if(n>0):
            tempat[n] = fib(n-1) + fib(n-2) + x[n]
        else:
            tempat[n] = 0
        return tempat[n]
 
n = int(input())
hasil = fib(n)
print(hasil)