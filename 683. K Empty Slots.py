class Solution(object):
    def kEmptySlots(self, bulbs, k):
        """
        :type bulbs: List[int]
        :type k: int
        :rtype: int
        """
        # 如果新打开的灯介于任何目标灯组之间，删除对应灯组
        def filterTargetList(target_list, b):
            new_list = []
            for t in target_list:
                start, end = sorted(t)
                if not (start <= b <= end):
                    new_list.append(t)
            return new_list

        # 如果有已经打开的灯，介于新打开的灯目标灯组之间，不必添加这个灯组
        def filterNewBulb(b1, b2, on_list):
            start, end = sorted([b1, b2])
            for o in on_list:
                if start <= o <= end:
                    return False
            return True

        
        # Step 1: Create empty list of target
        list_target = []
        count = 0
        on_list = []
        
        # Step 2: Went through the blubs list, record target
        for b in bulbs: 
            count += 1
            
            exist_in_target = any(b == y for x,y in list_target)
            if exist_in_target: 
                return count
            else: 
                list_target = filterTargetList(list_target, b)
                if b + k + 1 <= len(bulbs):
                    if filterNewBulb(b, b + k + 1, on_list):
                        list_target.append([b, b + k + 1])
                if b - k - 1 > 0:
                    if filterNewBulb(b, b - k - 1, on_list):
                        list_target.append([b, b - k - 1])
                on_list.append(b)
        return -1

我觉得这道题不难（变态），重要的是要考虑到新开的灯打破满足目标的灯组，以及已经打开的灯打破新开灯的目标灯组，及时删除多余的灯组。
复杂度 O(N)
