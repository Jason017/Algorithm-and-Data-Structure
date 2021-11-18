# 391. Number of Airplanes in the Sky (LintCode)
# https://www.youtube.com/watch?v=ihf8JjQdta0&ab_channel=%E5%8F%A4%E5%9F%8E%E7%AE%97%E6%B3%95
# 1:40

# 252. Meeting Rooms [https://leetcode.com/problems/meeting-rooms/]


class Solution:
    def countOfAirplanes(self, airplanes):
        """
        @param airplanes: An interval array
        @return: Count of maximum airplanes are in the sky.
        """
        nums = []
        
        for start, end in airplanes:
            nums.extend([start, end])
        pairs = sorted(list(enumerate(nums)), key=lambda x: x[1])
        
        mx, res = 0, 0
        for pair in pairs:
            if pair[0] % 2 == 0:
                mx += 1
            else:
                mx -= 1
            res = max(mx, res)
        return res


    def countOfAirplanes(self, airplanes):
        intervals=[]
        for start, end in airplanes:
            intervals.extend([(start, 1), (end, -1)])
        
        mx, ans = 0, 0
        intervals.sort()
        for _, cost in intervals:
            mx += cost
            ans = max(ans, mx)
        return ans

    
airplanes1 = [(1, 10), (2, 3), (5, 8), (4, 7)]
airplanes2 = [(1, 4), (2, 6), (3, 7), (4, 5)]
print(Solution().countOfAirplanes(airplanes1))
print(Solution().countOfAirplanes(airplanes2))


