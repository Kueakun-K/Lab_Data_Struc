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

input = [int(i) for i in input("Enter Input : ").split()]

li = []
inp = []
for i in range(len(input)):
    if input[i] < 0:
        li.append(i)
        li.append(input[i])
for i in input:
    if i >= 0:
        inp.append(i)
bbsort(inp)

while len(li) > 0:
    inp.insert(li.pop(0),li.pop(0))
for i in inp:
    print(i,end=" ")
