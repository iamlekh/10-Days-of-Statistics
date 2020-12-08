size = int(input())
numbers = list(map(int, input().split()))
weight = list(map(int, input().split()))

print(round(sum(map(lambda numbers,weight:numbers*weight,numbers,weight))/sum(weight),1))
