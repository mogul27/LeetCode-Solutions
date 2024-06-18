class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        profit_index = zip(profit, difficulty)
        sorted_index = sorted(profit_index, key=lambda x:x[0], reverse=True)
        max_profit = 0
        worker.sort(reverse=True)
        for w in worker:
            for pd_tup in sorted_index:
                # If difficulty of highest profit is doable
                if pd_tup[1] <= w:
                    max_profit += pd_tup[0]
                    break
        
        return max_profit
