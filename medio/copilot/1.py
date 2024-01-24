class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Inicializa a cabeça do nó de retorno e o nó de transporte
        head = ListNode(0)
        node = head
        carry = 0

        # Loop enquanto houver elementos em qualquer uma das listas ou o valor do transporte for diferente de zero
        while l1 or l2 or carry:
            # Obtém os valores dos nós atuais de ambas as listas, ou zero se a lista já tiver sido completamente percorrida
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)

            # Calcula a soma dos dois valores dos nós e do valor do transporte
            carry, out = divmod(val1+val2+carry, 10)

            # Cria um novo nó com o valor do resto da soma por 10 e adiciona-o à lista de retorno
            node.next = ListNode(out)
            node = node.next

            # Avança para o próximo nó em ambas as listas
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        # Retorna a lista de retorno
        return head.next