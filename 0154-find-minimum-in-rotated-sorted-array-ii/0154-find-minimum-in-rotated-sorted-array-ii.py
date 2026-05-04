class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        ans=float('inf')
        while low <= high:
            mid=(low+high)>>1
            if nums[low]==nums[mid]==nums[high]:
                ans=min(nums[mid],ans)
                low+=1
                high-=1
            elif nums[low] <= nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            elif nums[mid]<=nums[high]:
                ans=min(ans,nums[mid])
                high=mid-1
        return ans

            