n = int(input())
temp = n

reverse = 0

while(n>0):
    reverse = reverse * 10 + n%10
    n = n // 10

print(reverse)
if temp == reverse:
    print("True")
else:
    print("False")
