class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Crie um novo nó de cabeça para a nova lista ligada
        dummy = ListNode(0)
        
        while head:
            # Lembre-se do próximo nó
            next_node = head.next
            
            # Percorra a nova lista a partir da cabeça
            node = dummy
            while node.next and node.next.val < head.val:
                node = node.next
            
            # Insira o novo nó antes do nó maior
            head.next = node.next
            node.next = head
            
            # Vá para o próximo nó na lista original
            head = next_node
        
        return dummy.next