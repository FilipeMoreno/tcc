class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head  # If the list is empty or has only one element, it is already sorted.

        sentinel = ListNode(float('-inf'))  # Use a sentinel node.
        current = head

        while current:
            next_node = current.next
            prev = sentinel

            # Find the correct position to insert the current node in the sorted part.
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert the current node into the sorted part.
            current.next = prev.next
            prev.next = current

            current = next_node

        return sentinel.next
