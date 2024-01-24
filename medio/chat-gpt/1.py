class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            # Get the values from the current nodes or default to 0
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate the sum of current digits and carry
            total_sum = x + y + carry

            # Update carry for the next calculation
            carry = total_sum // 10

            # Update the current node with the remainder of the division
            current.next = ListNode(total_sum % 10)

            # Move to the next nodes in the input lists and the result list
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next

        return dummy_head.next
