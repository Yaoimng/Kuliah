memo = [-1 for _ in range(10**2)]
memo[1] = 1
memo[2] = 1
memo[3] = 2
memo[4] = 3
memo[5] = 5
memo[6] = 8
memo[7] = 13
memo[8] = 21


def f(n):
    if memo[n] != -1:
        return memo[n]
    else:
        if n > 0:
            memo[n] = f(n - 1) + f(n - 2)
        else:
            memo[n] = 0
        return memo[n]


def swap(arr, indeks1, indeks2):
    temp = arr[indeks1]
    arr[indeks1] = arr[indeks2]
    arr[indeks2] = temp


N = int(input())
hp = [input() for _ in range(N)]
M = int(input())
maps = [input().split() for _ in range(M)]

for i in range(M):
    memonya = int(maps[i][0])
    for j in range(N):
        if hp[j] == maps[i][1] and f(memonya) % 2 != 0:
            for k in range(N):
                if hp[k] == maps[i][2]:
                    swap(hp, j, k)
            break

for i in range(N):
    print(hp[i])
