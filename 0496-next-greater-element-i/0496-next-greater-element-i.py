class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hash={}
        stack=[]
        for num in nums2[::-1]:
            while stack and stack[-1]<=num:
                stack.pop()
            hash[num]=-1 if not stack else stack[-1]
            stack.append(num)
        ans=[hash[num] for num in nums1]
        return ans
                
            
            