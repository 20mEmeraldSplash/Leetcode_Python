from collections import deque
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        record = deque()
        record.append((0,1)) #初始情况
        visited = set((0,1))
        steps = 0

        while record:
            for _ in range(len(record)): 
                pos, speed = record.popleft()
                if pos == target:
                    return steps
                
                #A
                next_pos = pos + speed
                next_speed = speed * 2
                if (next_pos, next_speed) not in visited and 0 <= next_pos < target * 2: #不要走太远
                    record.append((next_pos, next_speed))
                    visited.add((next_pos, next_speed))
                
                #R
                next_pos = pos
                next_speed = -1 if speed > 0 else 1
                if (next_pos, next_speed) not in visited:
                    record.append((next_pos, next_speed))
                    visited.add((next_pos, next_speed))

            steps += 1 #每个for代表了广度优先搜索 (BFS) 的一层，也就是从当前层扩展到下一层的过程。
        return -1
 #复杂度：O(Target∗Log(Target))           
