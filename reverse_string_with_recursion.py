s = input()

def reversed(s):
    if len(s) == 1:
        return s
    return reversed(s[1:]) + s[0]

print(reversed(s))