def swap(arr, indeks1, indeks2):
    temp = arr[indeks1]
    arr[indeks1] = arr[indeks2]
    arr[indeks2] = temp

def fib(n):
    if n in {0, 1}:
        return n
    return fib(n - 1) + fib(n - 2)

N = int(input())
hp = [input() for _ in range(N)]

M = int(input())
maps = [input().split() for _ in range(M)]
fibonacci_list = []

for i in range(len(maps)):
    f = int(maps[i][0])
    fibonacci_list.append(fib(f))
#     print(f)

# print(fibonacci_list)
for i in range(M):
    for j in range(N):
        if hp[j] == maps[i][1]:
            for k in range(N):
                if hp[k] == maps[i][2] and fibonacci_list[i] % 2 !=0:
                    swap(hp, j, k)
                    break
            break
    

for i in range(N):
    print(hp[i])
