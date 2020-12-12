import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))

def meano(a):
    return round(sum(a)/len(a),1)
def mediano(a):
    i = len(a)%2
    ind = len(a)//2
    if i == 1:
        return sorted(a)[ind]
    else:
        return (sorted(a)[ind-1]+sorted(a)[ind])/2
def modeo(a):
    return max(set(a), key=a.count)

print(meano(numbers))
print(mediano(numbers))
print(int(stats.mode(numbers)[0]))

