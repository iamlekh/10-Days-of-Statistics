def gn(p,q,n):
    return (q**(n-1))*p


a, b = list(map(int, input().split(" ")))
n = int(input())
p = a/b
q = 1-p

x =0
for i in range(1,n+1):
    x += gn(p,q,i)


print(round(x,3))
