import heapq

nums = [15, 30, 10, 5]
heapq.heapify(nums) # O(N * log(N))
print(nums)

heapq.heappush(nums, 17) # O(log(N))
print(nums) 

heapq.heappop(nums) # O(log(N))
print(nums)


