from bisect import bisect_left
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    # Get the maximum height/depth of a binary tree
    def maxHeight(self, root):
        if root:
            return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right)) 
        return 0

    def maxHeight(self, root):
        if not root: return 0

        q = deque([root])
        depth = 0
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth


    # Deep copy a tree
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


    # Inorder Traversal of Binary Tree
    def inOrderRecur(self, root, output):
        if not root: return
        self.inOrderRecur(root.left, output)
        output.append(root.val)
        self.inOrderRecur(root.right, output)

    def inOrderIter(self, root):
        if not root: return []

        curr = root
        stack = []
        output = []

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                output.append(curr.val)
                curr = curr.right
        return output


    # Preorder Traversal of Binary Tree
    def preOrderRecur(self, root, output):
        if not root: return
        output.append(root.val)
        self.preOrderRecur(root.left, output)
        self.preOrderRecur(root.right, output)
    
    def preOrderIter(self, root):
        if not root: return []
    
        stack = [root]
        output = []
    
        while stack:
            curr = stack.pop()
            output.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return output


    # Postorder Traversal of Binary Tree
    def postOrderRecur(self, root, output):
        if not root: return
        self.postOrderRecur(root.left, output)
        self.postOrderRecur(root.right, output)
        output.append(root.val)

    # https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45648/three-ways-of-iterative-postorder-traversing-easy-explanation
    def postOrderIter(self, root):
        if not root: return []

        curr = root
        prev = TreeNode(None)
        stack = []
        output = []

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack[-1]
                if not curr.right or curr.right == prev:
                    output.append(curr.val)
                    stack.pop()
                    prev = curr
                    curr = None
                else:
                    curr = curr.right
        return output



class BST(TreeNode):
    def search(self, target):
        if not self or target == self.val:
            return self
        return self.left.search(target) if target < self.val \
            else self.right.search(target)

    def insert(self, root, value):
        if root:
            if root.val == value:
                return root
            elif root.val < value:
                root.right = self.insert(root.right, value)
            else:
                root.left = self.insert(root.left, value)
        else:
            return TreeNode(value)
        return root

    # Convert a List into a TreeNode
    def construct(self, nums):
        root = None
        for num in nums:
            root = self.insert(root, num)
        return root

    def bfs(self):
        q = deque([self])
        while q:
            node = q.pop()
            print(node.val)
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)


bst = BST(None)
root = BST(50)
bst.insert(root, 30)
bst.insert(root, 20)
bst.insert(root, 40)
bst.insert(root, 70)
bst.insert(root, 80)

# Test Iterative and Recursive Traversal
newTree = bst.construct([50,30,20,40,70,80])
print(bst.inOrderIter(newTree))

inOrder,preOrder,postOrder = [],[],[] 
bst.preOrderRecur(root, preOrder)
bst.inOrderRecur(root, inOrder)
bst.postOrderRecur(root, postOrder)
print("Pre Order Iterative Traversal:", bst.preOrderIter(root))
print("Pre Order Recursive Traversal:", preOrder, "\n")

print("In Order Iterative Traversal:", bst.inOrderIter(root))
print("In Order Recursive Traversal:", inOrder, "\n") # Ascending Order

print("Post Order Iterative Traversal:", bst.postOrderIter(root))
print("Post Order Recursive Traversal:", postOrder, "\n")


# https://stackoverflow.com/questions/26564646/space-complexity-of-iterative-vs-recursive-binary-search-tree
# Recursive BST vs Iterative BST in terms of time/space complexity


# Binary Search recursively
# O(log(n)) O(log(n))
def binary_search_recursive(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_recursive(arr, low, mid-1, target)
        elif arr[mid] < target:
            return binary_search_recursive(arr, mid+1, high, target)
    return -1

# Binary Search iteratively
# O(log(n)) O(1)
def binary_search_iterative(arr, target):
    mid, low, high = 0, 0, len(arr)
    while low <= high:
        mid = (low+high) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# Binary Search with Bisect
# O(log(n)) O(1)
def binary_search_bisect(arr, target):
    idx = bisect_left(arr, target) 
    if idx != len(arr) and arr[idx] == target: 
        return idx
    else: 
        return -1


arr = [2,3,4,10,40,50]
print(binary_search_recursive(arr, 0, len(arr)-1, 40))
print(binary_search_iterative(arr, 40))
print(binary_search_bisect(arr, 40))

