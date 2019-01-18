# encoding=utf-8

# 解题思路： 区分是否开始扫描数字的状态，如果没有开始碰到数据就xxx，如果碰到了数据就xxx；
# 根据字符串拼接数字的时候，直接把原来的数字*10，加上现在的数字，就可以，不需要用pow。
# mark: 分类讨论; 字符串


class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        result = 0
        start = False
        for i in s:
            # 非空格和数字开头:
            if not start:  # 未开始
                if i not in [' ', '-', '+', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    break
                elif not i:
                    continue
                elif i in ['-', '+']:
                    start = True
                    sign = -1 if i == '-' else 1
                    continue
                elif '0' <= i <= '9':
                    start = True
                    result = result * 10 + int(i)
                    continue
            else:
                if i < '0' or i > '9':  # 数字结束
                    break
                else:
                    result = result * 10 + int(i)

        result *= sign

        if result <= -2147483648:
            return -2147483648
        if result >= 2147483647:
            return 2147483647

        return result


if __name__ == "__main__":
    print Solution().myAtoi(" 42")
