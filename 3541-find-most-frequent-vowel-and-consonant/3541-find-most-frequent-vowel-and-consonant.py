class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels="aeiou"
        vow={}
        cons={}
        for i in s:
            if i in vowels:
                if i in vow:
                    vow[i]+=1
                else:
                    vow[i]=1
            else:
                if i in cons:
                    cons[i]+=1
                else:
                    cons[i]=1
        cntvow=0
        for key,value in vow.items():
            if cntvow < value:
                cntvow=value
        cntcons=0
        for key,value in cons.items():
            if cntcons < value:
                cntcons=value
        return cntvow+cntcons
            