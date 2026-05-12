class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans=[]
        xor=0
        for i in range(len(pref)):
            xor=xor^pref[i]
            ans.append(xor)
            xor=pref[i]
        return ans