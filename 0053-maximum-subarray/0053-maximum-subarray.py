class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        sum_=0
        for i in nums:
            sum_+=i
            if sum_<0:
                maxi=max(maxi,sum_)
                sum_=0
            else:
                maxi=max(maxi,sum_)
        return maxi            