import math
class Solution:
    def smallestDivisor(self,nums:List[int],threshold:int)->int:
        low=1
        high=max(nums)
        ans=high
        while low<=high:
            mid=(low+high)//2
            summ=0
            for num in nums:
                summ+=math.ceil(num/mid)
            if summ<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans