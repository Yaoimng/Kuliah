def swap(arr, indeks1, indeks2):
    temp = arr[indeks1]
    arr[indeks1] = arr[indeks2]
    arr[indeks2] = temp

N = int(input())
hp = [input() for _ in range(N)]

M = int(input())
map = [input().split() for _ in range(M)]

for i in range(M):
    for j in range(N):
        if hp[j] == map[i][0]:
            for k in range(N):
                if hp[k] == map[i][1]:
                    swap(hp, j, k)
                    break
            break

for i in range(N):
    print(hp[i])