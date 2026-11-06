class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low=1
        high=max(nums)
        ans=None
        while low<=high:
            mid=(low+high)>>1
            divisor=self.res(nums,mid,0)
            if divisor<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        
    def res(self,nums,div,val):
        for i in nums:
            val+=math.ceil(i/div)
        return val
                


       