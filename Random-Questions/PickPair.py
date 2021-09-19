class PickPair:
    def solution(nums,k):
        nums.sort()
        counter = 0
        while len(nums) >= 2 and nums[0]+nums[1] <= k:
            if nums[0]+nums[-1]<k:
                del nums[0]
            if nums[0]+nums[-1]>k:
                del nums[-1]
            else:
                counter+=1
                del nums[0]
                del nums[-1]
        return counter

    nums = [1,3,4,7,2,-1,7,4,3,0]
    print(solution(nums,5))