print(" *** String count ***")
x = input("Enter message : ").replace(" ","")
a = []
l = []
u = []

for i in x:
    a.append(i)
a.sort()

for j in a:
    if j.isalpha():
        if j.islower() :
            l.append(j)
        else:
            u.append(j)

b = len(u)
c = len(l)


if len(u) > 0:
    i = 0
    while i != len(u)-1:
        if u[i] == u[i+1]:
            u.pop(i)
            i = 0
        else:
            i = i+1
if len(l) > 0: 
    j = 0
    while j != len(l)-1 :
        if l[j] == l[j+1]:
            l.pop(j)
            j = 0
        else:
            j = j+1

print(f"No. of Upper case characters : {b}")
print("Unique Upper case characters : ",end="")
for y in u:
    print(y,end="  ")
print()

print(f"No. of Lower case Characters : {c}")
print("Unique Lower case characters : ",end="")
for z in l:
    print(z,end="  ")





