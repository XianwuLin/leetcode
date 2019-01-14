#encoding=utf-8

# 解题思路： 
# 每一位相加的结果只与左边数、右边数和进位有关，
# 计算出来的结果，个位数是当前的值，十位数是进位。
# 如果三者都不存在，则计算结束。
# 可以先生成一个Node，然后把指针保留着，最后返回指针的下一位。

from utils import ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        left_finish = right_finish = False
        first = result = ListNode(0)
        add = 0
        while True:
            if l1:
                left = l1.val
                l1 = l1.next
            else:
                left_finish = True
                left = 0
            if l2:
                right = l2.val
                l2 = l2.next
            else:
                right_finish = True
                right = 0
            if left_finish == right_finish == True and not add:
                break
            tmp = (left + right + add)
            if tmp >= 10:
                result.next = ListNode(tmp - 10)
                add = 1
            else:
                result.next = ListNode(tmp)
                add = 0
            result = result.next
        return first.next

if __name__ == "__main__":
    left = ListNode.list2chain([5])
    right = ListNode.list2chain([5])
    print Solution().addTwoNumbers(left, right)