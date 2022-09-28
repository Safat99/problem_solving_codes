roman = {'I':1, 'V': 5, 'X':10, 'C':100, 'M':1000, 'D':500, 'L':50}

s = 'LVIII' ## given string ... res 58

k = len(s)
i = 0
res = 0
flag = 0

while(i<k):
    print(s[i],i)
    if i+1 == k:
        flag = 1
        break
    if roman[s[i]] < roman[s[i+1]]:
        res += roman[s[i+1]] - roman[s[i]]
        i+=2
    else:
        res += roman[s[i]]
        i+=1

if flag == 1:
    res += roman[s[i]]

print("res", res)

