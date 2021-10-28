class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

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

q1 = Queue()
input = int(input("Enter choice : "))

if input == 1:
    q1.enQueue(10)
    q1.enQueue(20)
    q1.enQueue(30)
    print("Queue data : ",end="")
    for i in q1.item:
        print(i,end=" ")
    print()
    q1.deQueue()
    q1.enQueue(40)
    print("Size of Queue :",len(q1))
    print("Queue data : ",end="")
    for j in q1.item:
        print(j,end=" ")

elif input == 2:
    q1.enQueue(100)
    q1.enQueue(200)
    q1.enQueue(300)
    q1.deQueue()
    print("Queue data : ",end="")
    for i in q1.item:
        print(i,end=" ")
    print()
    print("Queue is Empty :",q1.isEmpty())

elif input == 3:
    q1.enQueue(11)
    q1.enQueue(22)
    q1.enQueue(33)
    q1.deQueue()
    q1.deQueue()
    q1.deQueue()
    if len(q1.item) == 0:
        print("Empty Queue")
    else:
        print("Queue data : ",end="")
        for i in q1.item:
            print(i,end=" ")
        print()
    print("Size of Queue :",len(q1))
    print("Queue is Empty :",q1.isEmpty())
