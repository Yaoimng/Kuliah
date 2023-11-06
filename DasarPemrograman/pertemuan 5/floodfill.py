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


def find_max_min_island_areas(matrix):
    max_area = 0
    min_area = float('inf')
    island_count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1: 
                area = flood_fill(matrix, i, j)
                print(f"{area}")
                max_area = max(max_area, area)
                min_area = min(min_area, area)
                island_count += 1

    return max_area, min_area, island_count

# Example usage:
# matrix = [
#     [1, 1, 0, 0, 0],
#     [1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 1],
#     [0, 0, 1, 0, 0],
# ]

matrix = [
    [1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
]
p = len(matrix)
print(p)
max_area, min_area, island_count = find_max_min_island_areas(matrix)
print(f"Max Island Area: {max_area}")
print(f"Min Island Area: {min_area}")
print(f"{island_count}")