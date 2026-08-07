class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash={}
        for i in t:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for i in s:
            if i in hash:
                hash[i]-=1
                if hash[i]==0:
                   del hash[i]
        st=""
        for i in hash:
            st+=i
        return st
            
        