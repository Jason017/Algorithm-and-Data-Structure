# In-place Function to Flatten Binary Tree into a Linked List
# The idea is to traverse through the nodes from left->right->root 
# and move every node to the right

# Here are three implementation provided below based on this youtube video
# https://www.youtube.com/watch?v=pCtXQ9XI7As&t=801s&ab_channel=FitCoder
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
        self.prev = None

    # Recursive Approach
    # O(N), O(N)
    def flatten(self, root):
        if not root: return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root

    # Stack Approach
    # O(N), O(N)
    def _flatten(self, root):
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            if stack:
                curr.right = stack[-1]
            curr.left = None

    # Similar to Morris Approach
    # O(N), O(1)
    def flatten_(self, root):
        while root:
            if root.left:
                prev = root.left
                while prev.right:
                    prev = prev.right
                prev.right = root.right
                root.right = root.left
                root.left = None
            root = root.right


    def toList(self, root):
        q = deque([root])
        output = []
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                output.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return output


    # Deep copy a tree with DFS
    # Similar Approach: LeetCode 133. Clone Graph
    def cloneTree(self, root):
        if not root: return None
        oldToNew = {root: TreeNode(root.val)}

        def dfs(node):
            if node.left:
                if node.left not in oldToNew:
                    oldToNew[node.left] = TreeNode(node.left.val)
                    dfs(node.left)
                oldToNew[node].left = oldToNew[node.left]
            if node.right:
                if node.right not in oldToNew:
                    oldToNew[node.right] = TreeNode(node.right.val)
                    dfs(node.right)
                oldToNew[node].right = oldToNew[node.right]

        dfs(root)
        return oldToNew[root]



treeNode = TreeNode(None)
root = TreeNode("A")
root.left = TreeNode("B")
root.left.left = TreeNode("C")
root.left.right = TreeNode("D")
root.right = TreeNode("E")
root.right.right = TreeNode("F")
root.right.right.left = TreeNode("G")

'''
Original Tree:
          A
        /   \
        B    E
       / \    \
      C   D     F
                /
                G

Flattended Tree:
    A
     \
      B
       \
        C
         \
          D
           \
            E
             \
              F
               \
                G
'''




root1 = treeNode.cloneTree(root)
print("Cloned Tree", treeNode.toList(root1))
treeNode.flatten(root1)
print("Flattening the Tree by Recursive Approach", treeNode.toList(root1))

root2 = treeNode.cloneTree(root)
print("Cloned Tree", treeNode.toList(root2))
treeNode._flatten(root2)
print("Flattening the Tree by Stack Approach", treeNode.toList(root2))

root3 = treeNode.cloneTree(root)
print("Cloned Tree", treeNode.toList(root3))
treeNode.flatten_(root3)
print("Flattening the Tree by Morris Approach", treeNode.toList(root3))
