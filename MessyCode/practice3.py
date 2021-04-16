# def missingNumber(nums):
#     for i in range(1,len(nums)+1):
#          if i not in nums:
#             return i

def missingNumber(nums):
    return sum(range(1,len(nums)+1)) - sum(nums)

lst1=[1,3,5,7,2,4,6,8,0]
print(missingNumber(lst1))

# Transpose a matrix with list comprehension
transposed = []
matrix = [[1,2,3,4],[4,5,6,8]]

for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

matrix = [[1,2],[3,4],[5,6],[7,8],[9,10]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)

# Try HashMap
print('Please enter an integer: ')
n = int(input().strip())
check = {True: "Not Weird", False: "Weird"}
print(check[n%2==0 and (n in range(2,6) or n > 20)])

# Floyd's tortoise and hare
# Solve findDuplicate in linear time and constant space
def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr2

# Using HashMap
def findDuplicate1(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return num
        seen[num] = True

print(findDuplicate([3,1,3,4,2]))

b = [2,7,11,15]
b = sorted([(num, i) for i, num in enumerate(b)])[::-1]
print(b)