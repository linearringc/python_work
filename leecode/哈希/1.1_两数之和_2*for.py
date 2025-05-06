class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]
        return[]

solution = Solution()

nums = [2, 4, 6]
target = 8

print(solution.twoSum(nums, target))