def sumOfTwoArr(a,b,v):
    diff = set()
    for i in range(len(a)):
        d = v-a[i]
        diff.add(d)
    for i in range(len(b)):
        if b[i] in diff:
            return True
    return False

# Brute Force:

# def sumOfTwoArr(a,b,v):
#     for i in range(len(a)):
#         diff_value = v-a[i]
#         for j in range(len(b)):
#             if b[j] == diff_value:
#                 return True
#     return False

a = [0,0,-5,3203]
b = [-10,40,-3,9]
v = -8
print(sumOfTwoArr(a,b,v))
