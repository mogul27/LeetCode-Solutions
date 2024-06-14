class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        move_counter = 0
        nums.sort()

        for index in range(1, len(nums)):
            # If the previous number is the same or smaller
            if nums[index] <= nums[index-1]:
                increment = nums[index-1] - nums[index] + 1
                nums[index] += increment
                move_counter += increment
            
        return move_counter
            
if __name__ == "__main__":
    solution = Solution()
    min = solution.minIncrementForUnique([3,2,1,2,1,7])
    print(min)
