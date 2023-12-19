def banyak_cara(n, m):
    if n == 100:
        return 1
    if n > 100 or n == m:
        return 0

    cara = 0
    for i in range(1, 7):
        posisi = n + i
        if posisi == m:
            continue
        elif posisi > 100:
            break
        else:
            cara += banyak_cara(posisi, m)
    return cara

n, m = map(int, input().split())
print(f"Ada {banyak_cara(n, m)} cara nih!")