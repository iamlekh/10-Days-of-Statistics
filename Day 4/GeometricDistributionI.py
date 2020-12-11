def gn(p,q,n):
    return (q**(n-1))*p


a, b = list(map(int, input().split(" ")))
n = int(input())
p = a/b
q = 1-p

print(round(gn(p,q,n),3))

