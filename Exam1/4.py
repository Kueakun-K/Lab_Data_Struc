print("*** String Rotation ***")
x,y = input("Enter 2 strings : ").split()
a = []
b = []
c = []
d = []
for i in x:
    a.append(i)
    c.append(i)
for j in y:
    b.append(j)
    d.append(j)

c.insert(0,c.pop())
d.append(d.pop(0))

x = 1
while c != a or d != b:
    if x <= 5:
        print(x,end=" ")
        for i in c:
            print(i,end="")
        print(" ",end="")
        for j in d:
            print(j,end="")
        print()
        c.insert(0,c.pop())
        d.append(d.pop(0))
        x = x+1
    else:
        c.insert(0,c.pop())
        d.append(d.pop(0))
        x = x+1
    
if x > 6:
    print(" . . . . .")
print(x,end=" ")
for i in c:
    print(i,end="")
print(" ",end="")
for j in d:
    print(j,end="")
print()
print(f"Total of  {x} rounds.")