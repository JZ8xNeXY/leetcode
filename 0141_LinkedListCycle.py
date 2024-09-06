# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast = head.next
        slow = head

        while slow != fast:
            if not fast or not fast.next:
                return False

            fast = fast.next.next
            slow = slow.next

        return True
