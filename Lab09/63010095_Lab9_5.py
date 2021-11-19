def bbsort(l):
    for i in range(len(l)-1):
        swape = False
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swape = True
        if not swape:
            break
    return l

def subset(inp,data,num,index=0,li=[]):
    sum = 0
    check = 0
    for i in li:
        sum += i
    if num == 0:
        if sum == data:
            print(li)
            return 1
        return 0
    elif index >= len(inp):
        return 0
    else:
        check += subset(inp,data,num-1,index+1,li+[inp[index]])
        check += subset(inp,data,num,index+1,li)

    return check
input = input("Enter Input : ").split("/")
inp = [int(i) for i in input[1].split()]
data = int(input[0])
bbsort(inp)
check = 0
for i in range(len(inp)):
    check += subset(inp,data,i+1)

if check == 0:
    print("No Subset")