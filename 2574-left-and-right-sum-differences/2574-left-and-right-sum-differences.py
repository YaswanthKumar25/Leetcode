class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        sum_=0
        rsum_=0
        n=len(nums)
        for i in range(n):
            left.append(sum_)
            sum_+=nums[i]
            j=n-i-1
            right.append(rsum_)
            rsum_+=nums[j]
        for i in range(len(left)):
            j=len(left)-i-1
            left[i]=abs(left[i]-right[j])
        return left
