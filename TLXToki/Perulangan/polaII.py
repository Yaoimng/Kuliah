n = int(input())

for i in range(n):
    for s in range(i, n-1):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print("*")
    