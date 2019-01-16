# encoding=utf-8

import json


class TreeNode(object):
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class Solution_v2(object):
    # 这种方法有点偷懒的意思，把二叉树转成了字典，
    # 然后借助json的dumps方法进行序列化和反序列化

    def dumps_dict(self, root):
        result = {}
        result['val'] = root.val
        if root.left is not None:
            result['left'] = root.left.dumps_dict()
        else:
            result['left'] = "#"
        if root.right is not None:
            result['right'] = root.right.dumps_dict()
        else:
            result['right'] = "#"
        return result

    def dumps(self, root):
        return json.dumps(root.dumps_dict())

    @staticmethod
    def loads_from_dict(data):
        result = TreeNode(data["val"])
        if data["left"] != "#":
            result.left = TreeNode.loads_from_dict(data["left"])
        if data["right"] != "#":
            result.right = TreeNode.loads_from_dict(data["right"])
        return result

    @staticmethod
    def loads(data):
        return TreeNode.loads_from_dict(json.loads(data))


class Solution:
    # 这种方法用了层序遍历，指针不需要上下跳动，需要一层一层地遍历，
    # 而且没有使用递归，要好一些。
    def serialize(self, root):
        if root is None:
            return "{}"

        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1

        while queue[-1] is None:
            queue.pop()

        nodes_list = list()
        for node in queue:
            if node is not None:
                nodes_list.append(str(node.val))
            else:
                nodes_list.append("#")
        return '{%s}' % ','.join(nodes_list)

    def deserialize(self, data):
        data = data.strip('\n')

        if data == '{}':
            return None

        vals = data[1:-1].split(',')

        root = TreeNode(int(vals[0]))
        queue = [root]
        isLeftChild = True
        index = 0

        for val in vals[1:]:
            if val is not '#':
                node = TreeNode(int(val))
                if isLeftChild:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)

            if not isLeftChild:
                index += 1
            isLeftChild = not isLeftChild

        return root


if __name__ == "__main__":
    pointer = TreeNode(23)
    # pointer.left = TreeNode(12)
    pointer.right = TreeNode(45)
    # pointer.left.left = TreeNode(44)
    # pointer.left.right = TreeNode(89)
    pointer.right.left = TreeNode(0)
    pointer.right.right = TreeNode(3)
    print Solution().serialize(pointer)
