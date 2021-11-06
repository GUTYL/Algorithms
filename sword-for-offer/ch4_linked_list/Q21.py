# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp_head = ListNode()
        tmp_head.next = head

        front = head
        back = tmp_head
        for i in range(n):
            front = front.next
        while front:
            front = front.next
            back = back.next
        back.next = back.next.next
        return tmp_head.next


node1 = ListNode()
node1.val = 1
node2 = ListNode()
node2.val = 2
node1.next = node2
node3 = ListNode()
node3.val = 3
node2.next = node3
node4 = ListNode()
node4.val = 4
node3.next = node4
node5 = ListNode()
node5.val = 5
node4.next = node5
s = Solution()
s.removeNthFromEnd(node1, 2)
