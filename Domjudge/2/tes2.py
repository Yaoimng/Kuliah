def flood_fill(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
        return 0

    matrix[i][j] = -1  # Mark the current cell as visited
    size = 1  # Initialize the size of the island

    # Check all neighboring cells
    size += flood_fill(matrix, i + 1, j)
    size += flood_fill(matrix, i - 1, j)
    size += flood_fill(matrix, i, j + 1)
    size += flood_fill(matrix, i, j - 1)

    return size

def peta(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1: 

n = 4
m = 5
matrix = [
[1, 1, 1, 0],
[1, 0, 1, 1],
[1, 0, 1, 0],
[0, 1, 1, 1],
[0, 0, 0, 1]
]
print (flood_fill(matrix, n, m))