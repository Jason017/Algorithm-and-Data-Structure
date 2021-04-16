# list[start:stop:step] # · start: index to start, inclusive (defaults to 0)
#                       # · stop:  index to stop,  exclusive (defaults to len)
#                       # · step:  slice by step             (defaults to 1)

# [1, 2, 3][:]   # → [1, 2, 3]
# [1, 2, 3][::2] # → [1, 3]
# [1, 2, 3][:1]  # → [1]
# [1, 2, 3][1:]  # → [2, 3]

# # ★ negative indexes wrap

# nums = list(range(0, 11)) # 11 elements
# nums[-5:]   # → [6, 7, 8, 9, 10]
# nums[-5:10] # → [6, 7, 8, 9]
# nums[:-2]   # → [0, 1, 2, 3, 4, 5, 6, 7, 8]
# nums[2:-2]  # → [2, 3, 4, 5, 6, 7, 8]


# import os
# absolute_path = os.path.abspath(__file__)
# print('Full path: ' + absolute_path)

def findTotalWays(arr, i, k): 
    if (k == 0 and i == len(arr)): 
        return 1
    if (i >= len(arr)):
        return 0
    return (findTotalWays(arr, i + 1, k) + 
            findTotalWays(arr, i + 1, k - arr[i]) + 
            findTotalWays(arr, i + 1, k + arr[i])) 

def print_element(input):
    if len(input) == 0:
        return
    else:
        removed = input[len(input)-1]
        input = input[:len(input)-1]
        print_element(input)
        print(removed)

def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)

L = range(10)
print(L[::-1])

scores = [54,67,48,99,27]
for i, score in enumerate(scores, 1):
    print(i, score)

def displaysublist(lst): 
    sublists = [[ ]] 
    for i in range(len(lst) + 1):   
        for j in range(i + 1, len(lst) + 1):         
           sub = lst[i:j] 
           sublists.append(sub) 
    return sublists

# lst = []
# n = int(input("Enter the size of the list: "))
# print("Enter the element of list: ")
# for i in range(int(n)):
#     k = int(input(""))
#     lst.append(k)
# print("All sublist: \n",displaysublist(lst)) 


given_list = [1, 2, [3], [4, [5, 6,[7,[8]]]]]
final_list = []
def flattenList(given_list):
    for x in given_list:
        if isinstance(x,list):
            flattenList(x)
        else:
            final_list.append(x)

flattenList(given_list)
print(final_list)


def longestSubstringLen(X, Y):
    m = len(X)
    n = len(Y)
    grid = [[0 for a in range(n+1)] for b in range(m+1)]
    result = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                grid[i][j] = 0
            elif X[i-1] == Y[j-1]:
                grid[i][j] = grid[i-1][j-1] + 1
                result = max(result, grid[i][j])
            else:
                grid[i][j] = 0
    return result
 
X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
 
print('Length of Longest Common Substring is', longestSubstringLen(X, Y))

lst=[3,5,7,1,8,1,7,0,9,6]

for i in range(len(lst)-1, -1, -1):
    print(lst[i], end=', ')

print()
print(lst, sep=', ')

print()
print(" cruel ".join(["hello", "world"]))

print()
print(",".join([str(i) for i in range(5)]))


# Try numpy
import numpy as np
A = np.array([[1, 1], [2, 1], [3, -3]])
print(A.transpose())