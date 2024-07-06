class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1 
        leftHeight = height[left]
        rightHeight = height[right]
        leftMax = leftHeight
        rightMax = rightHeight

        result = 0

        while left < right: 
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                result += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]
        return result

使用两个指针 left 和 right，分别从数组的两端向中间移动。
同时维护两个变量 leftMax 和 rightMax，分别记录左边和右边的最大高度。
在每一步中，根据 leftMax 和 rightMax 的较小值来决定哪一边的指针移动，并计算当前能装的水。
时间复杂度 O(n)，空间复杂度 O(1)。

