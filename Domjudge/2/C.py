def dfs(self, matrix, i, j, visited) :
    m = len(matrix)
    n = len(matrix[0]) 
    if i < 0 or j < 0 or i > m-1 or j > n-1 or matrix[i][j] == 0 or visited[i][j] :
        return
    visited[i][j] = False
    self.dfs(matrix, i-1, j, visited) 
    self.dfs(matrix, i+1, j, visited) 
    self.dfs(matrix, i, j-1, visited) 
    self.dfs(matrix, i, j+1, visited)

def hasPathDfs(self, matrix, sx, sy, dx, dy) :
    m = len(matrix)
    n = len(matrix[0])   
    visited = [[True for i in range(n)] for j in range(m)]
    self.dfs(matrix, sx, sy, visited)
    if visited[dx][dy] == True:
        return False
    return False


n,m = [int(V) for V in input().split()]
matrix = []
for i in range(m):
    matrix.append([int(V) for V in input().split()])