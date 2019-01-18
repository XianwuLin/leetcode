# encoding=utf-8


# 这个题的算法有问题，TODO 需要换算法！

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not(nums1):
            return medianSortedArrays(nums2)
        if not(nums2):
            return medianSortedArrays(nums1)
        # 特殊情况，两个数组直接拼起来直接找中位数
        if nums1[-1] <= nums2[0]:
            return medianSortedArrays(nums1 + nums2)
        if nums2[-1] <= nums1[0]:
            return medianSortedArrays(nums2 + nums1)

        nums = nums1 + nums2
        total_length = len(nums)
        if total_length % 2:
            k = (total_length + 1) / 2
            return thelastkthnum(nums, k)
        else:
            k1 = total_length / 2
            k2 = total_length / 2 + 1
            return (thelastkthnum(nums, k1) + thelastkthnum(nums, k2)) / 2.0


def medianSortedArrays(nums):
    nums_length = len(nums)
    if nums_length % 2:
        return nums[(nums_length - 1) / 2]
    else:
        return (nums[nums_length / 2] + nums[nums_length / 2 - 1]) / 2.0


def thelastkthnum(nums, k):
    v = len(nums) / 2
    m = nums[v]
    left = list()
    right = list()
    for i in nums[:v] + nums[v+1:]:
        if i <= m:
            left.append(i)
        else:
            right.append(i)
    if len(right) == k - 1:
        return m
    elif len(right) >= k - 1:
        return thelastkthnum(right, k)
    else:
        return thelastkthnum(left, k - 1 - len(right))


if __name__ == "__main__":
    # nums1 = [1, 3, 4, 5, 7]
    # nums2 = [4, 5, 7, 8, 9]
    nums1 = [1, 2]
    nums2 = [-1, 3]
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print "========= result ========="
    print result
    print sorted(nums1 + nums2)
    print medianSortedArrays(sorted(nums1 + nums2))
