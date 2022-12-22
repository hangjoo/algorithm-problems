from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_size = 0

        current_node = head
        while current_node is not None:
            node_size += 1
            current_node = current_node.next

        current_node = head
        for _ in range(1, node_size // 2 + 1):
            current_node = current_node.next

        return current_node
