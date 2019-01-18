# encoding=utf-8


# 解题思路： 不转成字符串，用栈保存数字，然后再挨个弹出
#
# mark: stack;

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= pow(-2, 31) or x >= pow(2, 31) - 1:
            return 0

        minus = 1
        if x < 0:
            minus = -1
            x = -x

        stack = list()
        while x:
            stack.append(x % 10)
            x = x / 10
        b = 0
        i = 0
        while stack:
            tmp = stack.pop()
            if tmp:
                b += tmp * pow(10, i)
            i += 1
        b *= minus

        if b <= pow(-2, 31) or b >= pow(2, 31) - 1:
            return 0
        return b


if __name__ == "__main__":
    print Solution().reverse(120)
