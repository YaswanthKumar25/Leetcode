class Solution:
    def maxDistinct(self, s: str) -> int:
        dic={}
        for i in s:
            dic[i]=1
        return len(dic)
        