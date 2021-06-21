### April 25th 
# Approach 1:
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
    # matrix[:] = [ [ row[i] for row in reversed(matrix)] for i in range(len(matrix)) ]
    # matrix[:] = map(list, zip(*reversed(matrix)))
    l = len(matrix)

    for j in range(l):
        for i in range(j,l):
            matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i] 

    for j in range(l):
        for i in range(l//2):
            matrix[j][i],matrix[j][l-i-1] = matrix[j][l-i-1],matrix[j][i]
# Approach 2:
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
