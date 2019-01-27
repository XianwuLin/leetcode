# encoding=utf-8

# 解题思路： 最经典的栈使用案例。
# 遇到左括号入栈，遇到右括号出栈，出栈的和右括号判断是否一致。
# 操作完后看栈内是否还有数据。

class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        data = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        for i in s:
            if i in data:
                stack.append(i)
            else:
                if not stack or (data[stack.pop()] != i):
                    return False
        return not stack

if __name__ == "__main__":
    print Solution().isValid("([")