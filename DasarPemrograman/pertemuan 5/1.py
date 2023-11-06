memo = [-1 for x in range(45)]
memo[0] = 1
memo[1] = 1
def f(n):
    if(memo[n]!=-1):
        return memo[n]
    else:
        if(n>0):
            memo[n] = f(n-1)+f(n-2)
        else:
            memo[n] = 0
        return memo[n]
n = int(input())
hasil = f(n-1)*125
print(hasil)