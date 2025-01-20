class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
