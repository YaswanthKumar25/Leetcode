class Solution:
    def mirrorDistance(self, n: int) -> int:
        k=str(n)
        k=k[::-1]
        k=int(k)
        return abs(n-k)