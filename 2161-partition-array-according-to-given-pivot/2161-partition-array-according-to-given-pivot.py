class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ans = [0] * n
        left = 0
        right = n - 1
        for i in range(n):
            if nums[i] < pivot:
                ans[left] = nums[i]
                left += 1
            j = n - 1 - i
            if nums[j] > pivot:
                ans[right] = nums[j]
                right -= 1
        while left <= right:
            ans[left] = pivot
            left += 1
        return ans