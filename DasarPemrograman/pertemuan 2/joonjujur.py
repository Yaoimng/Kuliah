def bilangan_prima(a):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def palindrom_prima(q):
    while True:
        if str(q) == str(q)[::-1] and bilangan_prima(q):
            return q
        q += 1

n = int(input())

for i in range(1, n+1):
    p = int(input())
    Terdekat = palindrom_prima(p)
    print(f'#{i} : {Terdekat}')