class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list1 = ['(', '[', '{']
        list2 = [')', ']', '}']
        reading_list = []
        for c in s:
            if c in list1:
                reading_list.append(c)
            else:
                if reading_list == []:
                    return False
                check_read_item = reading_list.pop(-1)
                if list2.index(c) != list1.index(check_read_item):
                    return False
        return reading_list==[]
