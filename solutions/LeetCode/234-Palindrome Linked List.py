from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []

        cur_node = head
        while cur_node is not None:
            values.append(cur_node.val)
            cur_node = cur_node.next

        if values == values[::-1]:
            return True
        else:
            return False
