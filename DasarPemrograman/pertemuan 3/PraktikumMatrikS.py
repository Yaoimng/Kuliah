n = int(input())
def matriksclockwise():
    result = []
    for i in range(n):
        row = list(map(int, input().split()))
        baris.append(row)
    
    for i in range(n):
        print(baris[0][i], end=" ")
    
    for i in range(1, n):
        print(baris[i][n - 1], end=" ")
    
    if (n > 1):
        for i in range(n - 1, -1, -1):
            print(baris[n - 1][i], end=" ")
        for i in range(n - 2, 0, -1):
            print(baris[i][0], end=" ")
    print(baris[1][1], end=" ")

matriksclockwise()