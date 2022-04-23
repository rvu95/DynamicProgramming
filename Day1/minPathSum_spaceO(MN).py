class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #[expr]*M will create M references of expression so instead go with [expr]*expr
        min_cost = [ [0 for m in range(len(grid[0]))] for n in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j ==0:
                    min_cost[0][0] = grid[0][0]
                elif i == 0:
                    min_cost[0][j] = grid[0][j-1] + min_cost[0][j-1]
                elif j == 0:
                    min_cost[i][0] = grid[i-1][0] + min_cost[i-1][0]
                else:
                    top = min_cost[i-1][j] + grid[i-1][j]
                    left = min_cost[i][j-1] + grid[i][j-1]
                    min_cost[i][j] = min(top, left)
        return min_cost[-1][-1]
                