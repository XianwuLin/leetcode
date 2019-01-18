# encoding=utf-8


# TODO 性能不行
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ps = ""
        ps_length = 0
        if len(s) <= 1:
            return s
        for i in xrange(len(s) - 1):
            for j in xrange(i+1, len(s)+1):
                tmp_length = j - i
                if tmp_length <= ps_length:
                    continue
                tmp = s[i:j]
                print i, j, tmp
                if self.stringIsPalindrome(s[i:j]):
                    ps = tmp
                    ps_length = tmp_length
        return ps

    def stringIsPalindrome(self, s):
        assert s
        k = len(s) / 2
        for i in range(k):
            if s[i] != s[-i - 1]:
                return False
        return True


def main():
    print Solution().longestPalindrome("babad")


if __name__ == "__main__":
    main()
