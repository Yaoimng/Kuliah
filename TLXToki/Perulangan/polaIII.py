n = int(input())
x = -1
for i in range(n):
    for j in range(i+1):
        x += 1
        y = x % 10
        print(y, end='')
    print(" ")