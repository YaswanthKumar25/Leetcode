class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[0]*len(nums)
        _sum=0
        for i in range(len(nums)):
            _sum+=nums[i]
            arr[i]=_sum
        return arr
        