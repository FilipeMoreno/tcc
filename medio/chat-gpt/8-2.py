class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # If the list is empty or has only one element, it is already sorted.

        sentinel = ListNode(float('-inf'))  # Use a sentinel node.
        current = head.next  # Start with the second node.
        last_sorted = head  # Pointer to the last node in the sorted part.

        while current:
            if current.val < head.val:
                # If the current node is smaller than the head, move the current node to the sorted part.
                head.next = current.next
                current.next = sentinel.next
                sentinel.next = current
                current = head.next
            else:
                # If the current node is greater than or equal to the head, find its correct position in the sorted part.
                prev = sentinel
                while prev.next and prev.next.val < current.val:
                    prev = prev.next
                head.next = current.next
                current.next = prev.next
                prev.next = current
                current = head.next

                if prev == last_sorted:
                    last_sorted = last_sorted.next
                else:
                    last_sorted = last_sorted  # No change in last_sorted if the current node is not moved.

        return sentinel.next
