#
# nPr = n!/ (n-r)!

n,r = map(int, input().split())
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

res = factorial(n) / factorial(n-r)
print("{}P{} result is".format(n,r),res)


def fact(n):
    "without recursion"
    res = 1
    if n<0:
        return None
    if n==0 or n==1:
        return 1
    while(n>1):
        res *= n
        n -= 1
    return res
res = fact(n) / fact(n-r)
print("{}P{} result is".format(n,r),res)

#### interesting approach from Anis vai !!!!
"""
6P4 means >> 6*5*4*3
6P2 means >> 6*5 (after katakati)
nPr means >> r times multiplication with dropping one
"""
res = 1
for i in range(n,n-r,-1):
    res *= i
print("{}P{} result is".format(n,r),res)






