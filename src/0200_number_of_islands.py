class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(r,c):
            if r<0 or c<0 or c==COLS or r==ROWS or grid[r][c] == "0":
                return True
            if (r,c) in visited:
                return True
            visited.add((r,c))
            return dfs(r+1, c) and dfs(r-1, c) and dfs(r,c+1) and dfs(r,c-1)
            

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c]=="1":
                    # print(r,c)
                    count += dfs(r,c)==True
                    # print(count)
        return count