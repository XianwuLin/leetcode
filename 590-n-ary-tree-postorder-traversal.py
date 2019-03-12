# encoding=utf-8

"""
使用栈+迭代（Iterative）
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = list()
        if not root:
            return res
        stack = [root]
        while stack:
            tmp = stack.pop()
            stack.extend(tmp.children)
            res.append(tmp.val)
        return res[::-1]