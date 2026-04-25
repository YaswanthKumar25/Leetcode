class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash={}
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]]+=1
            else:
                hash[nums[i]]=1
        for keys,values in hash.items():
            if values == 1:
                return keys