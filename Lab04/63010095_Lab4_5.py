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
    
    def pop(self,i):
        return self.items.pop(i)
    
    
class Stack():
    def __init__(self, ls = None):
        if ls == None:
            self.items = []
        else:
            self.items = list()     

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def checkmir():
    while not mir.isEmpty():
        if mir.size() > 2:
            if mir.items[-1] == mir.items[-2] == mir.items[-3]:
                item.enQueue(mir.pop())
                mir.pop()
                mir.pop()
            else:
                mirror.enQueue(mir.pop())
        else:
            mirror.enQueue(mir.pop())

def checkmirror():
    global mirrorcheck
    x = 0
    if mirror.isEmptry() == False and mirrorcheck == False:
        while not mirror.isEmptry():
            if x+2 < mirror.size():
                if mirror.items[x] == mirror.items[x+1] == mirror.items[x+2]:
                    item.enQueue(mirror.pop(x))
                    mirror.pop(x)
                    mirror.pop(x)
                    break
                else:
                    x += 1
            else:
                mirrorcheck = True
                break
    else:
        mirrorcheck = True

def checknor():
    global bomb, interrup
    while not nor.isEmpty():
        if nor.size() > 2:
            if nor.items[-1] == nor.items[-2] == nor.items[-3]:
                if item.size() > 0:
                    normal.enQueue(nor.pop())
                    normal.enQueue(nor.pop())
                    normal.enQueue(item.deQueue())
                    normal.enQueue(nor.pop())
                    interrup += 1
                else:
                    nor.pop()
                    nor.pop()
                    nor.pop()
                bomb += 1
            else:
                normal.enQueue(nor.pop())
        else:
            normal.enQueue(nor.pop())

def checknormal():
    global normalcheck , fail
    y = 0
    if normal.isEmptry() == False and normalcheck == False:
        while not normal.isEmptry():
            if y+2 < normal.size():
                if normal.items[y] == normal.items[y+1] == normal.items[y+2]:
                    normal.pop(y)
                    normal.pop(y)
                    normal.pop(y)
                    fail += 1
                    break
                else:
                    y += 1
            else:
                normalcheck = True
                break
    else:
        normalcheck = True
     
normal = Queue()
nor = Stack()
mirror = Queue()
mir = Stack()
item = Queue()

mirrorcheck = False
normalcheck = False
norcheck = False

bomb = 0
interrup = 0
fail = 0

input1 , input2 = input("Enter Input (Normal, Mirror) : ").split()

for i in input2:
    mir.push(i)
checkmir()
while mirrorcheck == False:
    checkmirror()
bombnum = item.size()
for i in input1[::-1]:
    nor.push(i)
checknor()
while normalcheck == False:
    checknormal()
normal.items.reverse()
mirror.items.reverse()

print("NORMAL :")
print(normal.size())
if normal.size() > 0:
    for i in normal.items:
        print(i,end="")
    print()
else:
    print("Empty")

if fail + interrup <= bomb:
    print(f"{bomb-interrup} Explosive(s) ! ! ! (NORMAL)")
elif bomb - fail >= 0:
    print(f"{bomb-fail} Explosive(s) ! ! ! (NORMAL)")
    print(f"Failed Interrupted {interrup} Bomb(s)")
else:
    print(f"{fail-bomb} Explosive(s) ! ! ! (NORMAL)")
    print(f"Failed Interrupted {interrup} Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(mirror.size())
if mirror.size() > 0:
    for i in mirror.items:
        print(i,end="")
    print()
else:
    print("ytpmE    ")
print(f"(RORRIM) ! ! ! (s)evisolpxE {bombnum}")