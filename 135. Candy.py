class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        result = [1 for r in ratings]
        for i in range (1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                result[i] = result[i-1]+1
        for j in range(len(ratings)-2, -1, -1): 
            if ratings[j]> ratings[j+1]:
                result[j] = max(result[j], result[j+1]+1)
        #print(result)
        return sum(result)

复杂度 O(n)
这道题不难，要想到正着一遍，反着一遍。
