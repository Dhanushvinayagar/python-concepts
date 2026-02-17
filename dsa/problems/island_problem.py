grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","1"]
]

def island():

    row = len(grid)
    col = len(grid[0])
    visited = set()
    count = 0

    def dfs(r,c):

        if r<0 or c<0 or r>=row or c>=col:
            return
        
        if (r,c) in visited:
            return
 
        if grid[r][c]=="0":
            return

        visited.add((r,c))

        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1" and (i, j) not in visited:
                dfs(i,j)
                count+=1

    print(count)
    return

island()