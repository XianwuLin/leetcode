# encoding=utf-8

# 最大的第k个值：
# 解题思路：利用快排，先用第一个作为标准值，分一波，分为左波，当前值，右波；
# 左波的每个值都小于当前值，右波的每个值都大于当前值；
# 如果右波的数量刚好等于k-1的话，当前值就是最大的第k个值；
# 如果右波的数量大于k-1的话，就接着对右波进行快排；
# 如果右波的数量小于k-1的话，就得从左波来找。


def thelastkthnum(nums, k):
    m = nums[0]
    left = list()
    right = list()
    for i in nums[1:]:
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
    nums = [11, 21, 31, 14, 51, 161, 7, 8, 9, 10]
    k = 5
    print thelastkthnum(nums, k)
