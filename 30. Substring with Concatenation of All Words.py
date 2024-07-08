class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        m = len(s)
        n = len(words[0])
        p = len(words)
        if n > m or not words: 
            return []
        
        windowSize = p * n
        result = []
        wordmap = {}
        for w in words:
            if w in wordmap:
                wordmap[w] += 1
            else:
                wordmap[w] = 1


        for i in range(n):
            left = i
            right = i
            hashmap = {}
            count = 0
            while right + n <= m:
                word = s[right : right + n]
                right += n
                if word in wordmap:
                    if word in hashmap:
                        hashmap[word] += 1
                    else:
                        hashmap[word] = 1

                    if hashmap[word] <= wordmap[word]:
                        count += 1
                    else:
                        while hashmap[word] > wordmap[word]:
                            left_word = s[left:left + n]
                            hashmap[left_word] -= 1
                            if hashmap[left_word] < wordmap[left_word]:
                                count -= 1
                            left += n

                    if count == p:
                        result.append(left)
                else:
                    hashmap.clear()
                    count = 0
                    left = right

        return result


代码的时间和空间复杂度总结
时间复杂度：O(m)，其中 m 是字符串 s 的长度。
空间复杂度：O(p)，其中 p 是单词列表 words 中单词的数量。
