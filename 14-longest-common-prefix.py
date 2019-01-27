# encoding=utf-8

# 解题思路： 挨个取字符进行遍历即可。


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        result = ""
        index = 0
        Flag = True
        while True:
            try:
                m = strs[0][index]
                for i in strs[1:]:
                    if i[index] != m:
                        Flag = False
                        break
            except:
                break
            if Flag:
                result += m
                index += 1
            else:
                break 
        return result

if __name__ == "__main__":
    print Solution().longestCommonPrefix(["dog","racecar","car"] )