f = [0 for x in range(41)]
f[1] = 1
f[2] = 5
f[3] = 11
while(1):
    N = int(input()) 
    for i in range(4,N+1):
        f[i] = f[i-1] + 4*f[i-2] + 2*f[i - 3]
    print(f[N])