import math

m, s = list(map(float, input().split(" ")))
a = float(input())
pf = float(input())
d = 2 ** 0.5

def c(x,m,s):
    return 0.5 * ( 1 + math.erf( (x-m) / (s * d)))

r1 = 100 - (c(a,m,s) * 100)
r2 = 100 - (c(pf,m,s) * 100) 
r3 = (c(pf,m,s) * 100)

print(round(r1,2))
print(round(r2,2))
print(round(r3,2))

