class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        cnt=0
        while j <= len(nums)-1:
            if nums[j]!=nums[i]:
                nums[i+1]=nums[j]
                j+=1
                i+=1
                cnt+=1
            else:
                j+=1
        return cnt+1