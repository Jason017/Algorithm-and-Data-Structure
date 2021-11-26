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

    def printInOrder(self):
        if self.left: self.left.printInOrder()
        print(self.val, end=" ")
        if self.right: self.right.printInOrder()

    def printPreOrder(self):
        print(self.val, end=" ")
        if self.left: self.left.printPreOrder()
        if self.right: self.right.printPreOrder()

    def printPostOrder(self):
        if self.left: self.left.printPostOrder()
        if self.right: self.right.printPostOrder()
        print(self.val, end=" ")

    def bfs(self):
        dq = deque([self])
        while dq:
            node = dq.pop()
            print(node.val)
            if node.left:
                dq.appendleft(node.left)
            if node.right:
                dq.appendleft(node.right)


root = TreeNode(50)
root.insert(root, 30)
root.insert(root, 20)
root.insert(root, 40)
root.insert(root, 70)
root.insert(root, 80)

print("\nIn Order: ")
root.printInOrder()
print("\nPre Order: ")
root.printPreOrder()
print("\nPost Order: ")
root.printPostOrder()
print()



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


# Get the maximum height/depth of a binary tree
def maxHeight(node):
    if node:
        return 1 + max(maxHeight(node.left), maxHeight(node.right)) 
    return 0

arr = [2,3,4,10,40,50]
print(binary_search_recursive(arr, 0, len(arr)-1, 40))
print(binary_search_iterative(arr, 40))
print(binary_search_bisect(arr, 40))

