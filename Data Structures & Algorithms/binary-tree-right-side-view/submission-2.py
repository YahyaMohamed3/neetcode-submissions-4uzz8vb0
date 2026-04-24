from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            rightSide = None
            for i in range(len(queue)):
                node = queue.popleft()
                rightSide = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(rightSide.val)
        return res
