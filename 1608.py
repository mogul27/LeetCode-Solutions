class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        for x in range(1, len(nums)+1):
            filtered_array = [num for num in nums if num >= x]
            if len(filtered_array) == x:
                return x
        
        return -1
