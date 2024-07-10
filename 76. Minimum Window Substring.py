from collections import Counter, defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        
        mapT = Counter(t)  # 计算可迭代对象中元素的出现次数
        requiredT = len(mapT)

        # 同时列出数据和数据下标
        filteredS = [(i, char) for i, char in enumerate(s) if char in mapT]

        window = defaultdict(int)
        lengthMin = float('inf')
        usedT = 0  # 需要 usedT = requiredT
        start = 0
        result = (0, 0)

        for end, (index, char) in enumerate(filteredS):
            window[char] += 1
            if window[char] == mapT[char]:
                usedT += 1
            
            # 当我们找到一个有效窗口时，尝试通过移动开始指针来最小化它
            while usedT == requiredT:
                start_char = filteredS[start][1]
                start_index = filteredS[start][0]
                
                # 更新最小窗口
                if index - start_index + 1 < lengthMin:
                    lengthMin = index - start_index + 1
                    result = (start_index, index + 1)
                
                # 移动窗口的开始
                window[start_char] -= 1
                if window[start_char] < mapT[start_char]:
                    usedT -= 1
                start += 1

        return s[result[0]:result[1]] if lengthMin != float('inf') else ""



时间复杂度：O(|S| + |T|)

创建 mapT (Counter(t))：O(|T|)
创建 filteredS：O(|S|)
主循环：虽然有嵌套循环，但每个字符最多被处理两次（一次被加入窗口，一次被移出窗口），所以复杂度仍然是 O(|S|)

空间复杂度：O(|S| + |T|)

mapT：O(|T|)
filteredS：最坏情况下为 O(|S|)，当 S 中的所有字符都在 T 中出现时
window：最坏情况下为 O(|T|)

其中 |S| 是字符串 S 的长度，|T| 是字符串 T 的长度。
