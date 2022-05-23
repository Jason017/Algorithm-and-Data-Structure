# https://paulonteri.notion.site/Sliding-Window-f6685a15f97a4ca2bb40111e2b264fb2#891e1ba6076b4454a9175a553393f295
def smallest_subarray_with_given_sum(nums, k):
    ans = float('inf')
    left = curr = 0

    for right in range(len(nums)):
        curr += nums[right]
        while left <= right and curr >= k:
            ans = min(ans, right-left+1)
            curr -= nums[left]
            left += 1

    if ans == float('inf'):
        return -1
    return ans

nums = [2,1,5,2,3,2]
k = 5
print(smallest_subarray_with_given_sum(nums, k))


def max_sub_array_of_size_k(nums, k):
    if len(nums) < k:
        return -1

    curr = ans = sum(nums[:k])

    for i in range(len(nums)-k):
        curr += nums[i+k] - nums[i]
        ans = max(curr, ans)

    return ans

nums = [2,1,5,1,3,2]
k=3 
print(max_sub_array_of_size_k(nums, k))
nums = [2,3,4,1,5]
k=2
print(max_sub_array_of_size_k(nums, k))
