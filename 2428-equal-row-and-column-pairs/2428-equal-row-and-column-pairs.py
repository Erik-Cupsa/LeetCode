class Solution(object):
    def equalPairs(self, grid):
        dic = {}
        for row in grid:
            rowStr = str(row)
            curr = dic.get(rowStr, 0)
            curr += 1
            dic[rowStr] = curr
        count = 0
        for j in range(len(grid)): 
            col = [grid[i][j] for i in range(len(grid))]
            colStr = str(col)
            count += dic.get(colStr, 0)
        return count
        