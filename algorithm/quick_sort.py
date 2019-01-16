# encoding=utf-8
import timeit


def quick_sort(data):
    # 最传统的快排
    m = data[0]
    left = list()
    right = list()
    for i in data[1:]:
        if i <= m:
            left.append(i)
        else:
            right.append(i)
    if len(left) > 1:
        left = quick_sort(left)
    if len(right) > 1:
        right = quick_sort(right)
    return left + [m] + right


def quick_sort_v2(data):
    # 使用了二叉树的快排，这个地方发现速度并没有比传统的快，主要的问题还是在最后序列化上。
    # 如果只构建二叉树的话，速度和传统的区别不大。
    # 我觉得传统的和使用了二叉树的原理都差不多，传统的更像是层序生成二叉树。

    class TreeNode(object):
        def __init__(self, val=None):
            self.val = val
            self.left = None
            self.right = None

        def add(self, val):
            if val <= self.val:
                if self.left is not None:
                    self.left.add(val)
                else:
                    self.left = TreeNode(val)
                    return
            else:
                if self.right is not None:
                    self.right.add(val)
                else:
                    self.right = TreeNode(val)
                    return

        def middleorder(self):
            result = list()
            if self.left is not None:
                result += self.left.preorder()
            result += [self.val]
            if self.right is not None:
                result += self.right.preorder()
            return result

    root = TreeNode(data[0])
    for i in data[1:]:
        root.add(i)
    return root.middleorder()


if __name__ == '__main__':
    data = [5, 2, 7, 3, 6]
    print quick_sort(data)
    print quick_sort_v2(data)
    print timeit.timeit("quick_sort([5, 2, 7, 3, 6])", setup="from __main__ import quick_sort")
    print timeit.timeit("quick_sort_v2([5, 2, 7, 3, 6])", setup="from __main__ import quick_sort_v2")
