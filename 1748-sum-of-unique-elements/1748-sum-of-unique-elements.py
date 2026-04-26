class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum_=0
        hash={}
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]]+=1
            else:
                hash[nums[i]]=1
        for key,value in hash.items():
            if value == 1:
                sum_+=key
        return sum_

        