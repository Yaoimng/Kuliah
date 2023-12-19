notes = [-1 for i in range(39)]
notes[0] = 9
notes[1] = 10 
notes[3] = 20

n = [0 for i in range(43)] 
n[2] = 1
n[3] = 0
n[4] = -1
n[5] = -2

for i in range(6,43):
    n[i] = n[i - 1] - 1

def fib(n):
    if(notes[n] != -1):
        return notes[n]
    else:
        if(n>0):
            notes[n] = fib(n-1) + fib(n-2) + n[n]
        else:
            notes[n] = 0
        return notes[n]


n = int(input())
hasil = fib(n)
print(hasil)