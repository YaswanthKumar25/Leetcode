class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower(nums,target):
            low=0
            high=len(nums)-1
            ans=len(nums)
            while low <= high:
                mid=(low+high)>>1
                if nums[mid] >= target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        def higher(nums,target):
            low=0
            high=len(nums)-1
            ans=len(nums)
            while low <= high:
                mid=(low+high)>>1
                if nums[mid] > target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        low=lower(nums,target)
        high=higher(nums,target)
        if low == len(nums) or nums[low] != target:
            return [-1,-1]
        else:
            return [low,high-1]
