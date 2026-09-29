class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash={}
        for i in range(len(stones)):
            if stones[i] in hash:
                hash[stones[i]]+=1
            else:
                hash[stones[i]]=1
        res=0
        for i in jewels:
            if i in hash:
                res+=hash[i]
        return res