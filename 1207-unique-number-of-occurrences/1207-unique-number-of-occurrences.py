class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash={}
        for i in range(len(arr)):
            if arr[i] in hash:
                hash[arr[i]]+=1
            else:
                hash[arr[i]]=1
        if len(hash.values())==len(set(hash.values())):
            return True
        else:
            return False
        