class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]
        for i in range(len(boxes)):
            sum_=0
            for j in range(len(boxes)):
                if boxes[j]=="1":
                    sum_+=abs(i-j)
            ans.append(sum_)
        return ans

