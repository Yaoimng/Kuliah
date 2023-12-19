def rotate_matrix(n, m, matrix):
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if m % 4 == 1:
                result[i][j] = matrix[j][n - 1 - i]
            elif m % 4 == 2:
                result[i][j] = matrix[n - 1 - i][n - 1 - j]
            elif m % 4 == 3:
                result[i][j] = matrix[n - 1 - j][i]
            elif m % 4 == 0:
                result[i][j] = matrix[i][j]

    for row in result:
        print(*row)

def main():
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        matrix = [list(map(int, input().split())) for _ in range(n)]
        
        rotate_matrix(n, m, matrix)

main()
