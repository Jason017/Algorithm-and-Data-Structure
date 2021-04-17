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

print(findDuplicate([3,1,4,4,2]))


# Decimal and binary conversion
def binaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def decimalToBinary1(num):
    if num == 0:
        return 0
    else:
        return num % 2 + 10 * decimalToBinary(num // 2)

def decimalToBinary(n):
    return bin(n).replace("0b","")

x = 1234
print('10011010010 in decimal: ', binaryToDecimal(10011010010))
print('1234 in binary: ', decimalToBinary(x))

lst = [a for a in bin(x).replace('0b','')]
res = [a for a in bin(x)[2:]]

print('lst: ',lst)
print('Find \'0\' in lst after index = 3: ',lst.index('0', 3))
print('Is lst equivalent to res? ',res == lst)

# Enumerate
x = [3,1,4,6,9]
for i, val in enumerate(x):
    print(i, val)

scores = [54,67,48,99,27]
# Starting index from 1
for i, score in enumerate(scores, 1):
    print(i, score)

# Array/List conversion
input_str_arr = input('Please enter an array: ').split()
print('Input string array: ', input_str_arr)
input_int_arr = [int(x) for x in input('Please enter an array: ').split()]
print('Input integer array: ', input_int_arr)

given_list = [1, 2, [3], [4, [5, 6,[7,[8]]]]]
def flattenList(given_list, final_list=[]):
    for x in given_list:
        if isinstance(x,list):
            flattenList(x)
        else:
            final_list.append(x)
    return final_list

print(flattenList(given_list))
