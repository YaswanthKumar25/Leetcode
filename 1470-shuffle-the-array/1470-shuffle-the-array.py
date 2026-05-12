class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        low=0
        high=n
        ans=[0]*(2*n)
        for i in range(len(ans)):
            if i % 2 ==0:
                ans[i]=nums[low]
                low+=1
            else:
                ans[i]=nums[high]
                high+=1
        return ans
            