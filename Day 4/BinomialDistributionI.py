a = list(map(float, input().split(' ')))

print(a)
def fac(n):
    return 1 if n == 0 else n*fac(n-1)


def com(n,s):
    return fac(n)/(fac(s) * fac(n-s))

def b(s,n,p):
    return com(n,s) * p ** s * (1-p)**(n-s)

p = a[0]/(a[0] + a[1])
n = 6

result = b(3,n,p) + b(4,n,p) + b(5,n,p) + b(6,n,p)
print(round(result, 3))
