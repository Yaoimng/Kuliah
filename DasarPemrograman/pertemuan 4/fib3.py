note = [-1 for x in range(35)]
note[1] = 0
note[2] = 1
note[3] = 2

def fib(n):
    if(note[n] != -1):
        return note[n]
    else:
        if(n > 0):
            note[n] = fib(n-3) + fib(n-2) + fib(n-1)
        else:
            note[n] = 0
        return note[n]

n = int(input())
ans = fib(n)
print(ans)