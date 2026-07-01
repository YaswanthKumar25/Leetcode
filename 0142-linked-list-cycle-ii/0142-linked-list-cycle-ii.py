# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash={}
        temp=head
        cnt=0
        while temp:
            if temp in hash:
                return temp
            else:
                hash[temp]=cnt
                cnt+=1
                temp=temp.next
        return None