def banyak_cara(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = banyak_cara(n - 1, memo) + banyak_cara(n - 3, memo) + banyak_cara(n - 5, memo)
    return memo[n]

s= int(input())
c = list(map(int, input().split()))
for val in c:
    hasil = banyak_cara(val)
    print(f"SESI {val}: {hasil}")
