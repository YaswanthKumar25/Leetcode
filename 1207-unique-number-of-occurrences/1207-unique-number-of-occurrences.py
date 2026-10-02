class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hash={}
        for i in arr:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        return len(set(hash.values()))==len(hash.values())
        
        