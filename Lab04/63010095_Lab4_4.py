class Queue():
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list   

    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmptry(self):
        return self.items == []

    def size(self):
        return len(self.items)

mqa = Queue()
mql = Queue()
yqa = Queue()
yql = Queue()

input = input("Enter Input : ").replace(":"," ").replace(","," ").split()
x = 0
i = j = 1
k = l = 1
while x < len(input):
    mqa.enQueue(input[x])
    mql.enQueue(input[x+1])
    yqa.enQueue(input[x+2])
    yql.enQueue(input[x+3])
    x += 4

print("My   Queue = ",end="")
print(f"{mqa.items[0]}:{mql.items[0]}",end="")
while i < mqa.size():
    print(f", {mqa.items[i]}:{mql.items[i]}",end="")
    i += 1
print()

print("Your Queue = ",end="")
print(f"{yqa.items[0]}:{yql.items[0]}",end="")
while j < yqa.size():
    print(f", {yqa.items[j]}:{yql.items[j]}",end="")
    j += 1
print()

ac1 = ac2 = lo1 = lo2 = ""
for a1 in mqa.items:
    ac1 += a1
for a2 in yqa.items:
    ac2 += a2
for l1 in mql.items:
    lo1 += l1
for l2 in yql.items:
    lo2 += l2
lista1 = ac1.replace("0","Eat ").replace("1","Game ").replace("2","Learn ").replace("3","Movie ").split()
lista2 = ac2.replace("0","Eat ").replace("1","Game ").replace("2","Learn ").replace("3","Movie ").split()
listl1 = lo1.replace("0","Res. ").replace("1","ClassR. ").replace("2","SuperM. ").replace("3","Home ").split()
listl2 = lo2.replace("0","Res. ").replace("1","ClassR. ").replace("2","SuperM. ").replace("3","Home ").split()

print("My   Activity:Location = ",end="")
print(f"{lista1[0]}:{listl1[0]}",end="")
while k < len(lista1):
    print(f", {lista1[k]}:{listl1[k]}",end="")
    k += 1
print()

print("Your Activity:Location = ",end="")
print(f"{lista2[0]}:{listl2[0]}",end="")
while l < len(lista2):
    print(f", {lista2[l]}:{listl2[l]}",end="")
    l += 1
print()

score = 0
z = 0
while z < mqa.size():
    if mqa.items[z] == yqa.items[z] and mql.items[z] == yql.items[z]:
        score += 4
    elif mqa.items[z] == yqa.items[z]:
        score += 1
    elif mql.items[z] == yql.items[z]:
        score += 2
    else:
        score -= 5
    z += 1

if score >= 7:
    print(f"Yes! You're my love! : Score is {score}.")
elif score > 0:
    print(f"Umm.. It's complicated relationship! : Score is {score}.")
else:
    print(f"No! We're just friends. : Score is {score}.")