def solve(n, arr):

    maxganjil = max(arr[::2], default=float('-inf'))
    ganjil = sum(x for x in arr[::2] if x > 0)

    maxgenap = max(arr[1::2], default=float('-inf'))
    genap = sum(x for x in arr[1::2] if x > 0)

    if ganjil > genap:
        print(f"Yosh, waktunya menyelamatkan Mob dengan {ganjil} spirit!")
    elif ganjil < genap:
        print(f"Yosh, waktunya menyelamatkan Mob dengan {genap} spirit!")
    else:
        max_spirit = max(maxganjil, maxgenap)
        print(f"Yosh, waktunya menyelamatkan Mob dengan {max_spirit} spirit!")

T = int(input())
for _ in range(T):
    N = int(input())
    spirits = list(map(int, input().split()))
    solve(N,spirits)
