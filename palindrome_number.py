class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

"""
prev Solution -->>
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        while(x>0):
            rev = rev*10 + x%10
            x = int(x/10)

        return rev == temp
"""
