# memo = [-1 for x in range(45)]
# memo[0] = 0
# memo[1] = 1
# def f(n):
#     if(memo[n]!=-1):
#         return memo[n]
#     else:
#         if(n>0):
#             memo[n] = n * f(n-1)
#         else:
#             memo[n] = 0
#         return memo[n]
# n = int(input())

# hasil = f(n)
# print(hasil)

def power(a,n):
    if n == 0:
        return 1
    else:
        return n * power(a, n-1)

# a = int(input())
# n = int(input())
# print(power(a,n))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)
    
n = int(input())
hasil = factorial(n)
print(hasil)
