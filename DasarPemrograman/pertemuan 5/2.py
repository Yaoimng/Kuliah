memo = [-1 for x in range(35)]
memo[1] = 0
memo[2] = 1
memo[3] = 2
#memo[n] = f(n)
#f(2) = memo[2] 
def f(n):
    if(memo[n] != -1):
        return memo[n]
    else:
        if(n>0):
            memo[n] = f(n-3) + f(n-2) + f(n-1)
        else:
            memo[n] = 0
        return memo[n]
# f(5)
# n = 5
# 
n = int(input())
hasil = f(n)
print(hasil)