from itertools import *

s = set()
for i in permutations("kkoooybbp", 3):
    s.add("".join(i))
print(len(s))

print(len(set(permutations("kkoooybbp", 3))))