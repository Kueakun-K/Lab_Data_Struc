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

q = Queue()
input = input("Enter Input : ").replace(","," ").split()
x = 0
while x < len(input):
    if input[x] == "E":
        q.enQueue(input[x+1])
        print(f"Add {input[x+1]} index is {q.size()-1}")
        x += 2
    else:
        if not q.isEmptry():
            print(f"Pop {q.deQueue()} size in queue is {q.size()}")
            x += 1
        else:
            print("-1")
            x += 1
if not q.isEmptry():
    print(f"Number in Queue is :  {q.items}")
else:
    print("Empty")
    
