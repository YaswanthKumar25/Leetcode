class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash={0:0}
        length=0
        maxlength=0
        sum_=0
        for i in range(len(nums)):
            sum_+=nums[i]
            rem=sum_-k
            if rem in hash:
                length+=1
            hash[sum_]=i
        return length
class Solution:
    def subarraySum(self, nums: List[int], k: int):
        prefix = {0: 1}
        total = 0
        sum_ = 0
        for num in nums:
            sum_ += num
            rem = sum_ - k
            if rem in prefix:
                total += prefix[rem]
                print(total)
            if sum_ in prefix:
                prefix[sum_] += 1
            else:
                prefix[sum_] = 1
        return total