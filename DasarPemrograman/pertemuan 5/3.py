memo = [-1 for x in range(39)]
memo[0] = 9
memo[1] = 10
memo[2] = 20
#memo[n] = f(n)
#f(2) = memo[2] 
x = [0 for x in range(43)]
x[2] = 1
x[3] = 0
x[4] = -1
x[5] = -2
for i in range(6,43):
    x[i] = x[i-1] - 1
def f(n):
    if(memo[n] != -1):
        return memo[n]
    else:
        if(n>0):
            memo[n] = f(n-1) + f(n-2) + x[n]
        else:
            memo[n] = 0
        return memo[n]
#kalau mau debug 
# for i in range(1,6):
    # print("f(",i,")  = ","f(",i-1,") + ","f(",i-2,")"," + x[",i,"]")
    # print("f(",i,")  = ",f(i-1), " + ",f(i-2)," + ",x[i],"")
n = int(input())
hasil = f(n)
print(hasil)