class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ans = 0
        st = set(nums)
        for x in st:
            if x - 1 in st:
                continue
            y = x + 1
            while y in st:
                y += 1
            ans = max(ans, y-x)
        return ans

solution = Solution()

nums = [100,4,200,1,3,2]

print(solution.longestConsecutive(nums))