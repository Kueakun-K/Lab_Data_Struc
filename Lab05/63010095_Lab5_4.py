
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
        self.previous = None 
    
class Linkedlist:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
            p.previous =t
        
    def insert(self,data):
        p = Node(data)
        t = self.head
        if t.data == "|":
            self.head = p
            p.next = t
            t.previous = p
        else:
            while t:
                if t.data == "|":
                    p.previous = t.previous
                    p.next = t
                    t.previous = p
                    p.previous.next = p
                    break
                else:
                    t = t.next  
    
    def left(self):
        t = self.head
        if t.data == "|":
            return 
        while t:
            if t.next.data == "|":
                t.data , t.next.data = t.next.data , t.data
                break
            else:
                t = t.next

    def right(self):
        t = self.head
        while t:
            if t.next == None:
                return
            if t.data == "|":
                t.next.data , t.data = t.data , t.next.data
                break
            else:
                t = t.next

    def backspace(self):
        t = self.head
        x = self.head
        if t.data == "|":
            return
    
        while t:
            if t.next.data == "|":
                break
            t = t.next
        while x:
            if x.next == t:
                break
            x = x.next
        next = t.next
        x.next = t.next
        t.previous = None
        t.next = None
        next.previous = x
           

    def delete(self):
        t = self.head
        while t:
            if t.next == None:
                return
            if t.data == "|":
                x = t
                t = t.next
                break
            else:
                x = t
                t = t.next
        x.next = t.next
        t = None
            

L = Linkedlist()
L.append("|")

input = input("Enter Input : ").split(",")

for i in input:
    if i[0] == "I":
        L.insert(i[2:])
    elif i[0] == "L":
        L.left()
    elif i[0] == "R":
        L.right()
    elif i[0] == "B":
        L.backspace()
    elif i[0] == "D":
        L.delete()
print(L)


