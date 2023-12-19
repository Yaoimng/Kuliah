def flood_fill(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
        return 0

    matrix[i][j] = 0  # Mark the current cell as visited
    size = 1  # Initialize the size of the island

    # Check all neighboring cells
    size += flood_fill(matrix, i + 1, j)
    size += flood_fill(matrix, i - 1, j)
    size += flood_fill(matrix, i, j + 1)
    size += flood_fill(matrix, i, j - 1)

    return size

def find_path(matrix, i, j):
  if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
    return True

  if flood_fill(matrix, i, j) == 0:
    return False

  if i < len(matrix) - 1 and matrix[i + 1][j] == 1:
    matrix[i + 1][j] = 0
    if find_path(matrix, i + 1, j):
      return True

  if j < len(matrix[0]) - 1 and matrix[i][j + 1] == 1:
    matrix[i][j + 1] = 0
    if find_path(matrix, i, j + 1):
      return True

  return False

n = 4
m = 5
matrix = [
[1, 1, 1, 0],
[1, 0, 1, 1],
[1, 0, 1, 0],
[0, 1, 1, 1],
[0, 0, 0, 1]
]

find_path(matrix, 4, 5)
print (matrix)