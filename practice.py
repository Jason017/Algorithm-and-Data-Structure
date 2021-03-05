# def q(target, aList, memo=set()):
#     if len(aList) == 0:
#         return False
#     num = aList.pop()
#     memo.add(num)    
#     if target + num in memo:
#         return True
#     return q(target, aList, memo)

def compareAll(lst, tgt):
    x = 0
    while x < len(lst): # let's call this x loop
        y = 0
        while y < len(lst): # let's call this y loop
            if abs(lst[x]-lst[y]) == tgt:
                return True
            y += 1
        x += 1
    return False

def recur_diff(lst, tgt, start, end):
    if (abs(lst[start]-lst[end])==tgt):
        return True
    if (start == end):
        return False
    if (start == end - 1):
        return recur_diff(lst, tgt, 0, start)
    return recur_diff(lst, tgt, start+1, end)

def recur(lst, tgt, start, end):
    if (end > len(lst) or start >= end):
        return False
    elif (abs(lst[start]-lst[end])==tgt):
        return True
    return recur(lst, tgt, start+1,end) or recur_diff(lst, tgt, start, end-1) 

def is_diff_two(lst, tgt):
    if not lst or len(lst) < 2:
        return False
    return recur_diff(lst, tgt, 0, len(lst)-1)

list1 = [3,4,1,3,-1,7]
list2 = [2,4,8]
list3 = [1,2,4,8,1]
list4 = [2,4,4,8]
list5 = [5]
list6 = [0,0,3,2,0,0]
list7 = [-1,5,4]
tgt1 = 4
tgt2 = 7
tgt3 = 0
tgt4 = 3
tgt5 = 1

# print(q(tgt1, list2, memo=set())) # True
print(is_diff_two(list1, tgt1)) # True
print(is_diff_two(list2, tgt1)) # True
print(is_diff_two(list3, tgt2)) # True
print(is_diff_two(list4, tgt2)) # False
print(is_diff_two(list5, tgt3)) # False
print(is_diff_two(list6, tgt1)) # False
print(is_diff_two(list7, tgt4)) # False

# aList = [0,0,0,0,0,0]
# aList[:1] = [1]
# aList[1:] = [2] * len(aList[1:])
# print(aList)

def compare_all_recur(lst, tgt, x=0, y=0):
    if(len(lst)-1 == x and len(lst) == y):
        return False
    if(len(lst) == x or len(lst) == y):
        return compare_all_recur(lst, tgt, x+1, 0)
    if(abs(lst[x] - lst[y])==tgt):
        return True
    return compare_all_recur(lst, tgt, x, y+1)

print()
print(compare_all_recur([2,3,4,5,6],0)) # True
print(compare_all_recur(list6,tgt5))