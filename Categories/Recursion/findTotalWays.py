def findTotalWays(arr, i, k):
    '''
    Given an integer array, find number of ways 
    to calculate a target number using only array 
    elements and addition or subtraction operator.
    '''
    if k == 0 and i == len(arr):
        return 1
    if i >= len(arr):
        return 0
    return findTotalWays(arr, i + 1, k) + findTotalWays(arr, i + 1, k - arr[i]) 

arr = [1, 2, 3]
k = 4
print(findTotalWays(arr, 0, k))

arr = [-3, 1, 3, 5, 7]
k = 6
print(findTotalWays(arr, 0, k))

arr = [2, 3, -4, 4]
k = 5
print(findTotalWays(arr, 0, k))


def find_max(stocks, k):
    ans = 0
    curr = 0
    n = len(stocks)
    seen = set()
    l = 0

    # O(n)
    for r in range(n):
        if stocks[r] in seen:
            for i in range(l, r):
                curr -= stocks[i]
                seen.remove(stocks[i])
                l += 1
        if r - l + 1 > k:
            curr -= stocks[l]
            seen.remove(stocks[l])
            l += 1
        curr += stocks[r]
        seen.add(stocks[r])
        ans = max(curr, ans)
    return ans

print(find_max([1, 2, 7, 7, 4, 3, 6], 3))

        # int ans = 0, curr = 0, n = stocks.length;
        # int l = 0, r = 0;
        # Set<Integer> seen = new HashSet<>();
        # for (; r < n; r++) {
        #     int num = stocks[r];
        #     if (seen.contains(num)) {
        #         for (; l < r; l++) {
        #             curr -= stocks[l];
        #             seen.remove(stocks[l]);
        #         }
        #     }
        #     if (r - l + 1 > k) {
        #         curr -= stocks[l];
        #         seen.remove(stocks[l++]);
        #     }
        #     curr += num;
        #     seen.add(num);
        #     ans = Math.max(curr, ans);
        # }
        # return ans;