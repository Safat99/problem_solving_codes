"""
Input is a given string and a numRow
--->> if input == "abcdefgh" rows 2
--->> output -->> "acegbdfh"
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        if numRows == 1:
            return s
        str_list = [""]*numRows
        m = 0
        i = 0
        switch = False
        while(i<l):
            if m == numRows - 1:
                switch = True
            if m == 0:
                switch = False
            if switch == False:
                str_list[m] += s[i]
                m +=1
            if switch == True:
                str_list[m] += s[i]
                m -=1
            
            i += 1
        return "".join(str_list)
