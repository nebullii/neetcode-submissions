"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Create copy of each node
        orig_head = head
        while head:
            copy = Node(head.val)
            copy.next = head.next
            head.next = copy
            head = head.next.next

        # Create copy of each random pointer
        head = orig_head
        copy_head = orig_head.next
        while head:
            copy = head.next
            if head.random:
                copy.random = head.random.next

            head = head.next.next

        # Split copy from original
        head = orig_head
        while head:
            copy = head.next
            next_orig = head.next.next
            head.next = next_orig

            if copy.next:
                copy.next = copy.next.next

            head = next_orig

        return copy_head

        