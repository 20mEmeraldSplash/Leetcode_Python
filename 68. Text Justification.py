class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        currentWidth = 0
        lastRow = []
        lastWidth = 0
        lastRowResult = ""
        for word in words: 
            if currentWidth + (len(lastRow) if lastRow else 0) + len(word) > maxWidth: 
                # 需要换行
                spaceWidth = maxWidth - lastWidth
                if len(lastRow) == 1:
                    lastRowResult = lastRow[0] + " " * spaceWidth
                else:
                    remainder = spaceWidth % (len(lastRow) - 1)
                    quotient = spaceWidth // (len(lastRow) - 1)
                    for i in range(len(lastRow)):
                        lastRowResult += lastRow[i]
                        if i != len(lastRow) - 1: 
                            lastRowResult += " " * (quotient + (1 if i < remainder else 0))
                
                result.append(lastRowResult)
                lastRow = []
                lastWidth = 0
                lastRowResult = ""
                currentWidth = 0
            
            lastRow.append(word)
            lastWidth += len(word)
            currentWidth += len(word)

        # 处理最后一行
        lastRowResult = " ".join(lastRow).ljust(maxWidth)
        result.append(lastRowResult)
        return result



时间复杂度: O(n)
空间复杂度: O(n)
