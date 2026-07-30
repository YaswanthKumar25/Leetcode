class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash={}
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]]+=1
            else:
                hash[nums[i]]=1
        print(hash)
        maxi=max(hash.values())
        sum_=0
        for val in hash.values():
            if val == maxi:
                sum_+=val
        return sum_
            
        