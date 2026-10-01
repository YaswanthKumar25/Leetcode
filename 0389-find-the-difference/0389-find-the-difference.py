class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash={}
        for i in s:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for i in t:
            if i in hash:
                hash[i]-=1
                if hash[i]==0:
                    del hash[i]
            else:
                hash[i]=1
        diff=''
        for i in hash.keys():
            diff+=i
        return diff