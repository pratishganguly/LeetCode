class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)]for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0]==0 else 0
        for i in range(m):
            for j in range(n):
                top = dp[i-1][j] if i > 0 and obstacleGrid[i][j]==0 else 0
                left = dp[i][j-1] if  j>0 and obstacleGrid[i][j]==0 else 0
                if i >0 or j>0:
                    dp[i][j] = top + left
        return dp[m-1][n-1]
