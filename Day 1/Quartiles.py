size = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)


ind = size//2

def mediano(a):
    i = len(a)%2
    indx = len(a)//2
    if i == 1:
        return sorted(a)[indx]
    else:
        return (sorted(a)[indx-1]+sorted(a)[indx])/2

if size % 2 == 0:
    data_low = numbers[0:int(size/2)]
    data_high = numbers[int(size/2):size]
else:
    data_low = numbers[0:int(size/2)]
    data_high = numbers[int(size/2)+1:size]

    
print(int(mediano(data_low)))
print(int(mediano(numbers[:])))
print(int(mediano(data_high)))
