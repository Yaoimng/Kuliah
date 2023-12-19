def flood_fill(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
        return 0

    matrix[i][j] = 0  
    size = 1  

    # Cek
    size += flood_fill(matrix, i + 1, j)
    size += flood_fill(matrix, i - 1, j)
    size += flood_fill(matrix, i, j + 1)
    size += flood_fill(matrix, i, j - 1)

    return size

def area_(matrix):
    island_count = 0
    s = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1: 
                area = flood_fill(matrix, i, j)
                s+= str(area) + " "
                island_count += 1
                        
    
    return s, island_count


m,n = [int(V) for V in input().split()]
matrix = []
for i in range(m):
    matrix.append([int(V) for V in input().split()])


s, island_count = area_(matrix)
print(f"Banyak Pulau: {island_count}")
print(f"Luas Pulau: {s}")