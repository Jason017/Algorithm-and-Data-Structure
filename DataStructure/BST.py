class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key

def insert(root, key) -> int:
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
        print(root.val, end=" ")
        inorder(root.right)


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

lst = str(inorder(r))
print()



# Binary Search
def binarySearch(arr, low, high, target):
    if high >= low:
        mid = (high+low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr, low, mid-1, target)
        elif arr[mid] < target:
            return binarySearch(arr, mid+1, high, target)
    return -1

arr = [2,3,4,10,40,50]
idx = binarySearch(arr, 0, len(arr)-1, 30)
print(idx)

# Get the maximum height/depth of a binary tree
def maxHeight(node):
    if node is None:
        return 0
    else:
        return 1 + max(maxHeight(node.left), maxHeight(node.right)) 
