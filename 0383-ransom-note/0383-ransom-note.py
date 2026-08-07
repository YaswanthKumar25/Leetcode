class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash={}
        for i in magazine:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for i in ransomNote:
            if i in hash:
                hash[i]-=1
                if hash[i]==0:
                    del hash[i]
            else:
                return False
        return True
            
