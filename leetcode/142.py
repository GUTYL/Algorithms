# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while True:
            if not fast or not fast.next:
                return None
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        fast = head
        while fast != slow:
            slow, fast = slow.next, fast.next
        return fast


s = Solution()
head = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(4)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n2

print(s.detectCycle(head))
