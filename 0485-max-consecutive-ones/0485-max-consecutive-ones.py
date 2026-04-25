class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcnt=0
        cnt=0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt=0
            else:
                cnt+=1
                maxcnt=max(cnt,maxcnt)
        return maxcnt
        