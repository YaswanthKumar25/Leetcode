class Solution:
    def isPalindrome(self, x: int) -> bool:
        original=x
        sum_=0
        if x < 0:
            return False
        while x>0:
            last=x%10
            sum_=(sum_*10)+last
            x//=10
        return True if sum_==original else False