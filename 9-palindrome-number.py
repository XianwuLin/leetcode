# encoding=utf-8

# 解题思路： 将数字转成列表，然后判断列表是不是回文的。
# 这种做法在python里不是最优的，但是按照算法来说，应该是比较好的做法。
# 按照python的做法，可以直接将数字转成字符串，然后反转比较是否一致。


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        tmp = list()
        while x:
            i = x % 10
            x = x / 10
            tmp.append(i)
        for i in xrange(len(tmp) / 2):
            if tmp[i] != tmp[-i - 1]:
                return False
        return True


if __name__ == "__main__":
    print Solution().isPalindrome(1)
