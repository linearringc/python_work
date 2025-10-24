class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target-num in hashtable:
                return[hashtable[target-num], i]
            else:
                hashtable[nums[i]] = i
        return []



solution = Solution()

nums = [2, 4, 6]
target = 10

print(solution.twoSum(nums, target))