#encoding=utf-8

# 解题思路： 用空间换时间，用字典把用过的数字保存起来，并建立索引
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = dict()
        for index, val in enumerate(nums):
            tmp = target - val
            if tmp in result:
                return [index, result[tmp]]
            else:
                result[val] = index


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print Solution().twoSum(nums, target)