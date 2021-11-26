from bisect import bisect_left
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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
    def constructBST(self, nums):
        root = None
        for num in nums:
            root = self.insert(root, num)
        return root

    # Get the maximum height/depth of a binary tree
    def maxHeight(self, root):
        if root:
            return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right)) 
        return 0

    def inOrderTraverse(self, root, output):
        if not root: return
        self.inOrderTraverse(root.left, output)
        output.append(root.val)
        self.inOrderTraverse(root.right, output)

    def preOrderTraverse(self, root, output):
        if not root: return
        output.append(root.val)
        self.preOrderTraverse(root.left, output)
        self.preOrderTraverse(root.right, output)


    def postOrderTraverse(self, root, output):
        if not root: return
        self.postOrderTraverse(root.left, output)
        self.postOrderTraverse(root.right, output)
        output.append(root.val)

    def bfs(self):
        dq = deque([self])
        while dq:
            node = dq.pop()
            print(node.val)
            if node.left:
                dq.appendleft(node.left)
            if node.right:
                dq.appendleft(node.right)


t = TreeNode(None)
root = TreeNode(50)
t.insert(root, 30)
t.insert(root, 20)
t.insert(root, 40)
t.insert(root, 70)
t.insert(root, 80)

output = []
t.inOrderTraverse(root, output)
print(output)

newTree = t.constructBST([50,30,20,40,70,80])

inOrder,preOrder,postOrder = [],[],[] 
t.preOrderTraverse(newTree, preOrder)
t.inOrderTraverse(root, inOrder)
t.postOrderTraverse(root, postOrder)
print("Pre Order:", preOrder)
print("In Order:", inOrder) # Ascending Order
print("Post Order:", postOrder)


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
    while low<=high:
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

