from bisect import bisect_left
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def bfs(self):
        dq = deque([self])
        while dq:
            node = dq.pop()
            print(node.val)
            if node.left:
                dq.appendleft(node.left)
            if node.right:
                dq.appendleft(node.right)


    def find(self, val):
        if val == self.val:
            return True
        elif val < self.val:
            if self.left == None:
                return False
            else:
                return self.left.find(val)
        else:
            if self.right == None:
                return False
            else:
                return self.right.find(val)

        
    def printInOrder(self):
        if self.left:
            self.left.printInOrder()
        print(self.val)
        if self.right:
            self.right.printInOrder()


def insert(root, val):
    if root:
        if root.val < val:
            root.right = insert(root.right, val)
        elif root.val > val:
            root.left = insert(root.left, val)
        else:
            return root
    else:
        return Node(val)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, high=" ")
        inorder(root.right)


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# lst = str(inorder(r))


# Binary Search recursively
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

