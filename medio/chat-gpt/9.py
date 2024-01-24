# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # Split the linked list into two halves
        middle = self.find_middle(head)
        second_half = middle.next
        middle.next = None

        # Recursively sort each half
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(second_half)

        # Merge the sorted halves
        sorted_list = self.merge(left_sorted, right_sorted)

        return sorted_list

    def find_middle(self, head):
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
        dummy = ListNode()
        current = dummy

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # If one of the lists is longer, append the remaining nodes
        if left:
            current.next = left
        elif right:
            current.next = right

        return dummy.next

# Example usage:
# Create a linked list: 4 -> 2 -> 1 -> 3
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
solution = Solution()
sorted_head = solution.sortList(head)

# Print the sorted linked list
while sorted_head:
    print(sorted_head.val, end=" ")
    sorted_head = sorted_head.next
