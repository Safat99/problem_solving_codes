## in this solution i have converted the string to an array and after repostion
## i have used join()

s = input("Enter given string: ")
l = len(s)
s = list(s)

for i in range(l//2):
    s[i], s[l-1-i] = s[l-1-i], s[i]

s = "".join(s)
print(s)