# encoding=utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils import ListNode


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        tmp = result
        while (l1 is not None) and (l2 is not None):
            if l1.val > l2.val:
                tmp.next = l2
                l2 = l2.next
            else:
                tmp.next = l1
                l1 = l1.next
            tmp = tmp.next
        if l1 is None:
            tmp.next = l2
        else:
            tmp.next = l1
        return result.next


if __name__ == "__main__":
    l1 = ListNode.list2chain([1, 2, 4])
    l2 = ListNode.list2chain([1, 3, 4])
    print Solution().mergeTwoLists(l1, l2)
