class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash={}
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]]+=1
            else:
                hash[nums[i]]=1

        for key,value in hash.items():
            if value > 1:
                return key