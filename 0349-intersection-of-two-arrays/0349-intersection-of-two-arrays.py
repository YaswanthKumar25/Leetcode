class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li=[]
        k=set(nums1)
        for i in nums2:
            if i in k:
                li.append(i)
        return list(set(li))
