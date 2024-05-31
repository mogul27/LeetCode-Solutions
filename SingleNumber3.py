class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        answer = set()
        for x in nums:
            if x in answer:
                answer.remove(x)
            else:
                answer.add(x)
        
        return answer
