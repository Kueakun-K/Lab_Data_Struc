def GreaterValue(l,i,r,x):
    if i > r:
        return "No First Greater Value"
    else:
        if l[i] > x:
            return l[i]
        else:
            return GreaterValue(l,i+1,r,x)

inp = input('Enter Input : ').split('/')
data = [int(i) for i in inp[0].split()]
check = [int(j) for j in inp[1].split()]
for k in check:
    print(GreaterValue(sorted(data),0,len(data)-1,k))