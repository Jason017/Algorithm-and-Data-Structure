from bisect import bisect_left

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root:
        if root.val < key:
            root.right = insert(root.right, key)
        elif root.val > key:
            root.left = insert(root.left, key)
        else:
            return root
    else:
        return Node(key)
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
    if node is None:
        return 0
    else:
        return 1 + max(maxHeight(node.left), maxHeight(node.right)) 


arr = [2,3,4,10,40,50]
print(binary_search_recursive(arr, 0, len(arr)-1, 40))
print(binary_search_iterative(arr, 40))
print(binary_search_bisect(arr, 40))

