size = int(input())
numbers = list(map(int, input().split()))

mean = sum(numbers)/size

sqd = sum(map(lambda numbers:(numbers-mean)**2,numbers))

print(round((sqd/size)**.5,1))
