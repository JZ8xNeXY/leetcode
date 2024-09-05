# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        prev = None

        while current:
            # 次のノードを一時的に保存
            next_node = current.next

            # 現在のノードのnextをprevに繋ぎなおす
            current.next = prev

            # prevを更新して現在のノードにする
            prev = current

            # currentを次のノードにする
            current = next_node

        return prev
