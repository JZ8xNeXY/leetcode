# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pointerA, pointerB = headA, headB

        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        return pointerA


listA = [4, 1, 8, 4, 5]
listB = [5, 6, 1, 8, 4, 5]

solution = Solution()
print(solution.getIntersectionNode())