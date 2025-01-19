class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)

        root.left, root.right = right_inverted, left_inverted

        return root
