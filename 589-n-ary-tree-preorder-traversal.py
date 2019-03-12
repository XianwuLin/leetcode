# encoding=utf-8


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = list()
        if root:
            res.append(root.val)
            for child in root.children:
                res.extend(self.preorder(child))
        return res


if __name__ == "__main__":
    pass
