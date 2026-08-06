class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        for word in strs:
            rev="".join(sorted(word))
            if rev in hash:
                hash[rev].append(word)
            else:
                hash[rev]=[word]
        arr=[]
        for i in hash.values():
            arr.append(i)
        return arr