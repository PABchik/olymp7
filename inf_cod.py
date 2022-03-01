t = 3 * 60
D = 16 * 10**3
i = 24
k = 4

free = 5 * 2**10 * 2**10 * 2**3

I = t * D * i * k

ans = (free - I) / 8 * -1
print(ans)