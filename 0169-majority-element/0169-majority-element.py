class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxi=0
        cnt=0
        for i in nums:
            if cnt == 0:
                maxi = i
                cnt+=1
            elif i != maxi:
                cnt-=1
            else:
                cnt+=1
        return maxi

        