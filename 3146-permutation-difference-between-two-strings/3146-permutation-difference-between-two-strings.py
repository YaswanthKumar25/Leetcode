class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        smap={}
        for i,j in enumerate(s):
            smap[j]=i
        res=0
        for i,j in enumerate(t):
            res+=abs(smap[j]-i)
        return res
