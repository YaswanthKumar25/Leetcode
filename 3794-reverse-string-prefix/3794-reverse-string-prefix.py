class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        s1=s[:k]
        s1=s1[::-1]
        s=s1+s[k:]
        return s
        