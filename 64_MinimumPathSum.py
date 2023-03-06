class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)]for _ in range(m)]
        dp[0][0] = grid[0][0]
        x = [0,1]
        y = [1,0]
        for i in range(m):
            for j in range(n):
                top = dp[i-1][j] if i > 0 else 1e9
                left = dp[i][j-1] if  j>0 else 1e9
                if i >0 or j>0:
                    dp[i][j] = grid[i][j] + min(top, left)
        return dp[m-1][n-1]
