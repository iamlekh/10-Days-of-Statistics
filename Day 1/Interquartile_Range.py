# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
numbers = list(map(int, input().split()))
freq= list(map(int, input().split()))

new = []

for i in range(size):
    for j in range(freq[i]):
        new.append(numbers[i])
new = sorted(new)
size = len(new)
ind = size//2

def mediano(a):
    i = len(a)%2
    indx = len(a)//2
    if i == 1:
        return sorted(a)[indx]
    else:
        return (sorted(a)[indx-1]+sorted(a)[indx])/2

if size % 2 == 0:
    data_low = new[0:int(size/2)]
    data_high = new[int(size/2):size]
else:
    data_low = new[0:int(size/2)]
    data_high = new[int(size/2)+1:size]
  

print(float(mediano(data_high)-mediano(data_low)))
