class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0 or len(s)==1:
            return len(s)
        maxcnt=0
        cnt=0
        i=0
        j=0
        st=""
        while j <= len(s)-1:
            if s[j] in st:
                st=""
                i+=1
                j=i
            elif s[j] not in st:
                st+=s[j]
                maxcnt=max(maxcnt,len(st))
                j+=1
                cnt+=1
        
        return cnt if maxcnt==0 else maxcnt



        