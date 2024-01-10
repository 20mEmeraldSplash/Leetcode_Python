class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        # I know should start from top-left, but not sure how to continue
        rows = len(grid)
        cols = len(grid[0])
        count = 0


        # My first time know that I can write extra function here
        def helper(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            # Actually I do not understand how to write next.
            # 使用 grid[i][j] = '0' 的目的是为了标记已经访问过的陆地单元格。这样做有两个主要目的：
            # 防止重复访问：在进行深度优先搜索（DFS）时，我们不想重复访问已经检查过的单元格。如果不将它们标记为已访问（例如，将其值改为'0'），我们可能会再次遇到这些单元格并错误地将它们计算为新的岛屿的一部分。这会导致对岛屿数量的错误计算。
            #有效地区分陆地和水：一旦我们访问了一个陆地单元格（值为'1'），我们就通过将其值更改为'0'来标记它，这样在后续的搜索中就可以将其视为水域。这意味着任何从其他路径到达这个单元格的搜索都会忽略它，因为它现在被视为水（'0'）而不是陆地。
            grid[r][c] = '0'
            helper(r-1, c)
            helper(r+1, c)
            helper(r, c-1)
            helper(r, c+1)

        for r in range(rows):
            for c in range(cols):
                # If it is "1", we need to check if there are land/water around it
                if grid[r][c] == "1":
                    # Do something to check
                    helper(r, c)
                    count += 1
        return count
