import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search boundaries
        low, high = 1, max(piles)
        
        def canFinish(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h
        
        while low < high:
            mid = (low + high) // 2
            if canFinish(mid):
                high = mid  # Try a smaller k
            else:
                low = mid + 1  # Increase k
        
        return low
