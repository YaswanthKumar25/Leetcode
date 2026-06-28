class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr=[0]*(len(gain)+1)
        _sum=0
        for i in range(len(gain)):
            _sum+=gain[i]
            arr[i+1]=_sum
        return max(arr)