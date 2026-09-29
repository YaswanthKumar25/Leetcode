class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash={}
        for i in range(len(s)):
            if s[i] in hash:
                hash[s[i]]+=1
            else:
                hash[s[i]]=1
        for i in range(len(t)):
            if t[i] in hash:
                hash[t[i]]-=1
                if hash[t[i]]==0:
                    del hash[t[i]]
        if hash:
            return False
        return True