# encoding=utf-8

"""
用递归的方式，将树的比较落到子树的比较上，这样的话就能化归问题。
"""
from tree import TreeNode, deserialize, drawtree

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isa(root.left, root.right)


    def isa(self, left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return self.isa(left.right, right.left) and self.isa(left.left, right.right)
        return False

if __name__ == "__main__":
    node = deserialize('[1,2,2,null,3,null,3]')
    # drawtree(node)
    print Solution().isSymmetric(node)