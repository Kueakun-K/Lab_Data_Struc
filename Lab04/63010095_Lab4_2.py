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

mq = Queue()
q1 = Queue()
q2 = Queue()
input = list(input("Enter people : "))
time = 0 
x = 0
for i in input:
    mq.enQueue(i)

while not mq.isEmptry():
    time += 1
    
    if time == 4+(3*x) and q1.isEmptry() == False:
        q1.deQueue()
        x += 1
    if time % 2 == 0 and q2.isEmptry() == False:
        q2.deQueue()
    
    if q1.size() < 5:
        q1.enQueue(mq.deQueue())
    else:
        q2.enQueue(mq.deQueue())
    print(f"{time} {mq.items} {q1.items} {q2.items}")
    

    



