class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hash={}
        ans=[]
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]]+=1
            else:
                hash[nums[i]]=1
        for key,value in hash.items():
            if value  == 1:
                ans.append(key)
        return ans