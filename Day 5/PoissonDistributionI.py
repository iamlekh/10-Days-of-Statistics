import math
def fact(n):
    return 1 if n == 0 else n*fact(n-1)

m = float(input())
k = float(input())
p = ((m**k)*(math.exp(-m)))/fact(k)
print(round(p,3))
