import math
m, s = list(map(float, input().split(" ")))

a = float(input())
b1 , b2 = list(map(float, input().split(" ")))
d = 2 ** 0.5
def c(x,m,s):
    return 0.5 * ( 1 + math.erf( (x-m) / (s * d)))


r1 = c(a,m,s)
r2 = c(b2,m,s) - c(b1,m,s) 

print(round(r1,3))
print(round(r2,3))

