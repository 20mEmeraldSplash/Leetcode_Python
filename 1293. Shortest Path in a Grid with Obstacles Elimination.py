import Queue
class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        if rows == 1 and cols == 1:
            return 0
        
        queue = Queue.Queue()
        queue.put((0, 0, k, 0))  # (x, y, remaining obstacles that can be removed, steps)
        visited = set()
        visited.add((0, 0, k))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while not queue.empty():
            x, y, remaining_k, steps = queue.get()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols:
                    new_k = remaining_k - grid[nx][ny]
                    
                    if new_k >= 0 and (nx, ny, new_k) not in visited:
                        if nx == rows - 1 and ny == cols - 1:
                            return steps + 1
                        visited.add((nx, ny, new_k))
                        queue.put((nx, ny, new_k, steps + 1))
        
        return -1


主要修改内容：
使用队列进行广度优先搜索：这使得代码更清晰，并且适用于这种需要找到最短路径的情况。
修复方向检查逻辑：确保所有四个方向（上、下、左、右）都被正确检查。
改进访问记录的方法：通过集合记录 (x, y, remaining_k) 来避免重复访问。
代码解释：
queue.put((0, 0, k, 0))：从起点 (0, 0) 开始，初始剩余可消除障碍物的次数为 k，初始步数为 0。
visited.add((0, 0, k))：记录起点 (0, 0) 和剩余 k 次消除机会。
使用方向数组 directions 来表示四个可能的移动方向。
在 BFS 循环中，检查每个方向的下一个位置 (nx, ny) 是否在网格内，并计算新的剩余可消除障碍物的次数 new_k。
如果新的位置和剩余消除次数 new_k 有效且未访问过，则将其加入队列和访问集合中。

O(Rows∗Cols)
