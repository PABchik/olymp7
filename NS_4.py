from itertools import *

for i in permutations("0123"):
    s = "".join(i)
    a = s[2] + s[0] + s[2] + s[0]
    b = s[0] + s[1] + s[0] + s[1]
    c = s[0] + s[3] + s[0] + s[3] + s[3]

    if int(a, 4) + int(b, 4) == int(c, 4):
        print(a)
        print(b)
        print(s)
        



