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

def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def luffy_journey(matrix, start):
    islands, island_count = area_(matrix)
    islands.sort(key=lambda x: (distance(start, (x[0], x[1])), -x[2]))

    print("Route for Luffy Journey:")
    for i, island in enumerate(islands):
        print(f"Island {island_count - i} (Distance: {distance(start, (island[0], island[1]))}, Area: {island[2]})")


m,n = [int(V) for V in input().split()]
matrix = []
for i in range(m):
    matrix.append([int(V) for V in input().split()])


s, island_count = area_(matrix)
print(f"Banyak Pulau: {island_count}")
print(f"Luas Pulau: {s}")