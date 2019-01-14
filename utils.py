#encoding=utf-8

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        result = ""
        while True:
            result += str(self.val)
            if self.next is not None:
                result += " -> "
                self = self.next
            else:
                break
        return result

    @classmethod
    def list2chain(self, la):
        la = la[::-1]
        node = ListNode(la.pop())
        first = node
        while la:
            node.next = ListNode(la.pop())
            node = node.next
        return first
        



if __name__ == "__main__":
    print ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print ListNode.list2chain([2,3,4,5])
