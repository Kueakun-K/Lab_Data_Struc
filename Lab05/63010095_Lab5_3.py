class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
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
        

    def addHead(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            p.next = t
            self.head = p
        
    def reverse(self):
        p = self.head
        q = None
        while p != None:
            next = p.next
            p.next = q
            q = p
            p = next
        self.head = q
        
def merge(h1,h2):
    x = Node(0)
    tail = x
    while h1 != None:
        tail.next = h1
        h1 = h1.next
        tail = tail.next
    while h2 != None:
        tail.next = h2
        h2 = h2.next
        tail = tail.next

    return x.next

list1 = LinkedList()
list2 = LinkedList()

l1,l2 = input("Enter Input (L1,L2) : ").split()
l1 = l1.replace("-","").replace(">"," ").split()
l2 = l2.replace("-","").replace(">"," ").split()

for i in l1:
    list1.append(i)

for i in l2:
    list2.append(i)

print(f"L1    : {list1}")
print(f"L2    : {list2}")

list2.reverse()
list1.head = merge(list1.head, list2.head)
print(f"Merge : {list1}")
