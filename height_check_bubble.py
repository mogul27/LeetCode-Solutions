class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Sort the array to get expected using bubble sort
        expected = heights[:]

        for i in range(len(expected) - 1):
            swapped = False
            for j in range(len(expected)-i-1):
                if expected[j] > expected[j+1]:
                    swapped = True
                    expected[j], expected[j+1] = expected[j+1], expected[j]
            
            if not swapped:
                break

        # Use sets to compare the differences
        difference_counter = 0
        for i, height in enumerate(heights):
            if height != expected[i]:
                difference_counter += 1
        
        return difference_counter
