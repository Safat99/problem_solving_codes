class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        switch = 0
        if x<0:
            x = -1 * x
            switch = 1
        while(x>0):
            r = r * 10 + x % 10
            x = x // 10
        if switch == 1:
            r = -1 * r
        if  (-2**31 > r or r > 2**31-1):
            return 0
        return r

