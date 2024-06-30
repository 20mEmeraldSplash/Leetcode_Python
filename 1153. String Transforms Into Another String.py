class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if str1 == str2:
            return True
        # 检查字符的唯一映射
        hashtable = {}
        for s1, s2 in zip(str1, str2):
            if s1 in hashtable:
                if hashtable[s1] != s2:
                    return False
            else:
                hashtable[s1] = s2

        # 检查字符集大小
        # 如果 str2 使用了所有 26 个字母，且 str1 和 str2 形成一个闭环，就无法完成转换
        if len(set(str2)) == 26:
            return False
        return True

  #没有考虑到变成闭环的情况（谁能考虑到）
