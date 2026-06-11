class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head.next
        temp = head
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        if cnt == n:
            return head.next
        cnt = cnt - n - 1
        temp = head
        while cnt:
            temp = temp.next
            cnt -= 1
        temp.next = temp.next.next
        return head