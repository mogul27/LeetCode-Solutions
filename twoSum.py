class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for j in range(1, len(nums)):
            for index in range(len(nums) - j):
                if target - nums[index + j] == nums[index]:
                    return [index, index+j]
