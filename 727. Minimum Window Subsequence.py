class Solution(object):
    def minWindow(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: str
        """
        l1, l2 = len(s1), len(s2)
        m, n = 0, 0
        result = []

        while m < l1:
            if s1[m] == s2[n]:
                n += 1
                if n == l2:  # s2最后一位
                    end = m + 1
                    start = end - 1
                    while n > 0:
                        if s1[start] == s2[n-1]:
                            n -= 1
                        start -= 1
                    start += 1  # 调整 start 到正确的位置
                    result.append([start, end])
                    m = start  #从新的起点继续寻找
                    n = 0  # 重置 n
            m += 1

        if not result:
            return ""

        min_len = float("inf")
        min_window = ""
        for start, end in result:
            if end - start < min_len:
                min_len = end - start
                min_window = s1[start:end]

        return min_window


O(N)
