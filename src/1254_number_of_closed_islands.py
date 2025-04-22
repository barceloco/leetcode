class Solution:
    # def closedIsland(self, grid: List[List[int]]) -> int:
    def closedIsland(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLS:
                return False
            if grid[r][c]==1 or (r,c) in visited:
                return True
            visited.add((r,c))
            return dfs(r-1,c) and dfs(r+1,c) and dfs(r,c-1) and dfs(r,c+1)

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0 and (r,c) not in visited:
                    count += 1 if dfs(r,c) else 0
        return count
        
            

        # visited = set()
        # Nx, Ny = len(grid[0]), len(grid)
        # count = 0
        
        # def dfs(x,y):
        #     if x<0 or x>=Nx or y<0 or y>=Ny:
        #         return False
        #     if (x,y) in visited :
        #         return True
        #     visited.add((x,y))
        #     if grid[y][x] == 1:
        #         return True
        #     return dfs(x+1,y) and dfs(x-1,y) and dfs(x,y-1) and dfs(x,y+1)
        
        # for j in range(Ny):
        #     for i in range(Nx):
        #         if grid[j][i]==0 and (i,j) not in visited and dfs(i,j):
        #             count += 1
        
        # return count


grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]
        
# grid = [[0,0,1,1,0,1,0,0,1,0],
#         [1,1,0,1,1,0,1,1,1,0],
#         [1,0,1,1,1,0,0,1,1,0],
#         [0,1,1,0,0,0,0,1,0,1],
#         [0,0,0,0,0,0,1,1,1,0],
#         [0,1,0,1,0,1,0,1,1,1],
#         [1,0,1,0,1,1,0,0,0,1],
#         [1,1,1,1,1,1,0,0,0,0],
#         [1,1,1,0,0,1,0,1,0,1],
#         [1,1,1,0,1,1,0,1,1,0]]


s = Solution()
print(s.closedIsland(grid))
