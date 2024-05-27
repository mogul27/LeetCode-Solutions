class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        print(l1)
        print(l2)
        return_list_head = ListNode()
        carry_bit = 0

        # Head node
        node_sum = l1.val + l2.val + carry_bit
        if node_sum >= 10:
            carry_bit = 1
            node_sum -= 10

        return_list_head.val = node_sum
        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            node_sum = l1.val + l2.val + carry_bit
            
            if node_sum >= 10:
                carry_bit = 1
                node_sum -= 10
            else:
                carry_bit = 0

            current = return_list_head
            while current.next:
                current = current.next
            current.next = ListNode(node_sum)

            l1 = l1.next
            l2 = l2.next

        # Entering here means one list longer than the other so exhaust remaining
        while l1:
            if carry_bit:
                next_val = l1.val + carry_bit

                if next_val >= 10:
                    carry_bit = 1
                    next_val -= 10
                else:
                    carry_bit = 0
                
                current = return_list_head
                while current.next:
                    current = current.next
                current.next = ListNode(next_val)
            
            else:
                current = return_list_head
                while current.next:
                    current = current.next
                current.next = ListNode(l1.val)

            l1 = l1.next

        while l2:
            if carry_bit:
                next_val = l2.val + carry_bit

                if next_val >= 10:
                    carry_bit = 1
                    next_val -= 10
                else:
                    carry_bit = 0
                
                current = return_list_head
                while current.next:
                    current = current.next
                current.next = ListNode(next_val)

            else:
                current = return_list_head
                while current.next:
                    current = current.next
                current.next = ListNode(l2.val)
            l2 = l2.next
        
        # If carry bit left over once lists exhausted
        if carry_bit:
            current = return_list_head
            while current.next:
                current = current.next
            current.next = ListNode(1)

        return return_list_head
