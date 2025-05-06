class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        if not nums:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
