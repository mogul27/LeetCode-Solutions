class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Sort the array to get expected
        expected = sorted(heights)
        # Use sets to compare the differences
        difference_counter = 0
        for i, height in enumerate(heights):
            if height != expected[i]:
                difference_counter += 1
        
        return difference_counter
