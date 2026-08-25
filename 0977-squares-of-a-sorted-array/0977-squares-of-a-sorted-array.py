class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=[0]*len(nums)
        left=0
        right=len(nums)-1
        maxi=right
        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                arr[maxi]=abs(nums[right]**2)
                right-=1
                maxi-=1
            elif abs(nums[left])>abs(nums[right]):
                arr[maxi]=abs(nums[left]**2)
                left+=1
                maxi-=1
        return arr

