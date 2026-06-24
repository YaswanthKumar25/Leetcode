class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        t1 = headA
        t2 = headB
        while t1 != t2:
            t1 = t1.next if t1 else headB
            t2 = t2.next if t2 else headA
        return t1
