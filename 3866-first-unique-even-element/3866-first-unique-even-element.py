class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        cnt=0
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        for keys,values in dic.items():
            if keys%2 == 0 and values == 1:
                cnt=keys
                break
        return cnt if cnt>0 else -1
        