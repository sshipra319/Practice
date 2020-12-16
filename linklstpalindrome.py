def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        a = []
        while head:
            a.append(head.val)
            head = head.next
            
        return a == a[::-1]
        