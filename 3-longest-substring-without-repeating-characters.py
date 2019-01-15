# encoding=utf-8

# 解题思路：
# 依旧用了空间换时间的思路，记录找到的每个没有重复的子串的长度，然后求这些长度的最大值。
# 这里需要注意发现字符a已经在上一个子串中的时候，下一个子串应该是从上一个子串的a的下一位开始，而不是从a开始。


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = [0]
        now = ""
        for index, val in enumerate(s):
            if val not in now:
                now += val
                first[-1] += 1
            else:
                now = now[now.index(val) + 1:] + val
                first.append(len(now))
        return max(first)


if __name__ == "__main__":
    data = [
        "dvdf",
    ]
    for i in data:
        print i, "\t\t\t", Solution().lengthOfLongestSubstring(i)
