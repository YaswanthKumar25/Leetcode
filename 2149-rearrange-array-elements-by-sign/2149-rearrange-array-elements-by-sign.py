class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        i=0
        j=1
        k=0
        while i <= len(nums) and j <= len(nums):
            nums[i]=pos[k]
            i+=2
            nums[j]=neg[k]
            j+=2
            k+=1
        return nums


