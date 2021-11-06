# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node_list = []
        # 节点数为空
        if not head:
            return None
        while head.next:
            if head in node_list:
                return head
            node_list.append(head)
            head = head.next

    def detectCycle_update1(self, head: ListNode) -> ListNode:
        """集合替代list更新"""
        node_list = set()
        # 节点数为空
        if not head:
            return None
        while head.next:
            if head in node_list:
                return head
            node_list.add(head)
            head = head.next

    def get_node_in_loop(self, head):
        """判断是否有环，无环返回None，有环返回环中的一个节点"""
        if head is None or head.next is None:
            return None
        slow = head.next
        fast = slow.next
        while slow is not None and fast is not None:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        return None

    def detectCycle_update2(self, head: ListNode) -> ListNode:
        """快慢指针更新，需要知道环中节点数目的解法"""
        # 判断是否有环，无环返回None，有环返回环中的一个节点
        in_loop = self.get_node_in_loop(head)
        if not in_loop:
            return None
        loop_count = 1
        n = in_loop
        while n.next != in_loop:
            n = n.next
            loop_count += 1
        fast = head
        for i in range(loop_count):
            fast = fast.next
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow

    def detectCycle_update3(self, head: ListNode) -> ListNode:
        """快慢指针更新，不需要知道环中节点数目的解法"""
        # 判断是否有环，无环返回None，有环返回环中的一个节点
        in_loop = self.get_node_in_loop(head)
        if not in_loop:
            return None
        node = head
        while node != in_loop:
            node = node.next
            in_loop = in_loop.next
        return node


node1 = ListNode(3)
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(0)
node2.next = node3

node4 = ListNode(-4)
node3.next = node4
node4.next = node2

s = Solution()
print(s.detectCycle_update3(node1).val)
