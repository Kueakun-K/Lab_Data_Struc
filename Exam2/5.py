class Queue:
    def __init__(self,ls = None):
        if ls == None:
            self.item = []
        else:
            self.item = list()

    def __str__(self):
        return str(self.item)

    def __len__(self):
        return len(self.item)

    def enQueue(self,data):
        self.item.append(data)

    def deQueue(self):
        self.item.pop(0)

    def isEmpty(self):
        return self.item == []

    def check(self):
        x = len(self.item)
        for i in range(0,x):
            for j in range(0,x):
                if self.item[j] == self.item[i] and j != i:
                    return "Duplicate"
        return "NO Duplicate"


B = Queue()

x,y = input("Enter Input : ").split("/")

x = x.split()
for i in x:
    B.enQueue(i)

y = y.replace(","," ").split()

z = 0
while z != len(y):
    if y[z] == 'D':
        B.deQueue()
        z += 1
    elif y[z] == 'E':
        B.enQueue(y[z+1])
        z += 2

print(B.check())

    