class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        # divide a lista em duas metades
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        start = slow.next
        slow.next = None
        # ordena as duas metades
        l1 = self.sortList(head)
        l2 = self.sortList(start)
        # mescla as duas metades
        return self.merge(l1, l2)
    
    def merge(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        dummy = p = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 or l2
        return dummy.next