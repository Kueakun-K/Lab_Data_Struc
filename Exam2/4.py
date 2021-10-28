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
        s = ''
        p = self.head
        s +=str(p.data)
        p = p.next
        while p != None :
            s += ' <- '+str(p.data)
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
            p.previous = t 
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

    def reorder(self):
        p = self.head
        if p.data != "0":
            q = self.head
            x = self.tail
            t = self.head
            while p.next.data != "0":
                p = p.next
            q = p.next
            p.next = None
            x.next = t
            self.head = q
        else:
            return
        
        


li = LinkedList()

print(" *** Re order ***")
input = input("Enter Input : ").split()

for i in input:
    li.append(i)

print(f"Before : {li}")

li.reorder()
print(f"After : {li}")