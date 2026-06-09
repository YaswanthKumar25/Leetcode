import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) >> 1

            target = self.possible(piles, mid)

            if target <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low

    def possible(self, nums, mid):
        summ = 0

        for num in nums:
            summ += math.ceil(num / mid)

        return summ