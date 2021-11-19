def bbsort(l,num):
    for i in range(len(l)-1):
        swape = False
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                num[j], num[j+1] = num[j+1], num[j]
                swape = True
        if not swape:
            break
    return num

input = input("Enter Input : ").split()
data = []
num = []
for x in range(len(input)):
    for i in input[x]:
        if i.isalpha():
            num.append(ord(i))
            data.append(input[x])

bbsort(num,data)
for i in data:
    print(i,end=" ")