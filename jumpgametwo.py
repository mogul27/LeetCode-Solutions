class Solution:
    def jump(self, nums: list[int]) -> int:
        
        target_index = len(nums) - 1
        jump_counter = 0

        while target_index != 0:
            # Find nodes in order which can reach target
            for index, val in enumerate(nums):
                if index + val >= target_index:
                   target_index = index
                   jump_counter += 1
                   break

        return jump_counter
