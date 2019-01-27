# encoding=utf-8

# 解题思路： 强行解答，没啥难度

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        vdict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        mdict = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        if not s:
            return 0

        if len(s) == 1:
            return vdict[s]
        
        flag = False
        value = 0
        for i in xrange(len(s)):
            if flag:
                flag = False
                continue
            if len(s) - 1 == i:
                value += vdict[s[i]]
                break
            if s[i] + s[i+1] in mdict:
                flag = True
                value += mdict[s[i] + s[i+1]]
            else:
                value += vdict[s[i]]
         
        return value

if __name__ == "__main__":
    print Solution().romanToInt('MCMXCIV')