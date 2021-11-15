from bisect import bisect_right, bisect_left, bisect

def findKLargest(nums, k):
    arr = []
    for i in range(k): 
        mx = float('-inf')
        for j in range(len(nums)):
            if nums[j] > mx:
                mx = nums[j];
        nums.remove(mx);
        arr.append(mx)
          
    return arr[-1]

nums = [1000,298,3579,100,200,-45,900]
k = 2
print(findKLargest(nums, k))