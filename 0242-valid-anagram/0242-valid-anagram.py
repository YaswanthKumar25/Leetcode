class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
            else:
                return False
        if not hash:
            return True
        return False
        