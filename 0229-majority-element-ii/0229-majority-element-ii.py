class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt, cnt1 = 0, 0
        ele, ele1 = None, None  
        for i in nums:
            if i == ele:
                cnt += 1
            elif i == ele1:
                cnt1 += 1
            elif cnt == 0:
                ele = i
                cnt = 1
            elif cnt1 == 0:
                ele1 = i
                cnt1 = 1
            else:
                cnt -= 1
                cnt1 -= 1
        ans = []
        cnt = cnt1 = 0
        for i in nums:
            if i == ele:
                cnt += 1
            elif i == ele1:
                cnt1 += 1
                
        if cnt > len(nums) // 3:
            ans.append(ele)
        if cnt1 > len(nums) // 3:
            ans.append(ele1)
            
        return ans