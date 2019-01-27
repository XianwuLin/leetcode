# encoding=utf-8

# 解题思路： 从两边遍历数组，首先最大面积就是(right - left) * min(right_height, left_height)。
# 然后，如果left_height 小于 right_height，则 right -> right - 1 这种情况肯定比原来的小, 
# 但是 left -> left + 1 这种情况有可能比原来的大，然后依次取最大值就得到了最终的最大面积。
# 参考 https://www.cnblogs.com/zichi/p/5745992.html


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) == 1:
            return 0
        max_area = 0
        lindex = 0
        rindex = len(height) - 1
        while lindex < rindex:
            max_area = max(max_area, min(height[lindex], height[rindex]) * (rindex - lindex))
            if height[lindex] < height[rindex]:
                lindex += 1
            else:
                rindex -= 1
        return max_area

if __name__ == "__main__":
    print Solution().maxArea([1,8,6,2,5,4,8,3,7])