class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash={}
        for i in range(len(arr)):
            if arr[i] in hash:
                hash[arr[i]]+=1
            else:
                hash[arr[i]]=1
        return len(hash.values())==len(set(hash.values()))
        