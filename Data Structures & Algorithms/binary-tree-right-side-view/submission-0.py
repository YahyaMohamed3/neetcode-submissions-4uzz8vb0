from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])

        while q:
            rightSide = None
            for i in range(len(q)):
                node = q.popleft()
                rightSide = node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(rightSide.val)

        return res