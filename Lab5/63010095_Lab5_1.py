class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.sizee = 0

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
        self.sizee += 1

    def addHead(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            p.next = t
            self.head = p
        self.sizee += 1

    def search(self, item):
        x = self.head
        while x != None:
            if x.value == item:
                return "Found"
            x = x.next
        return "Not Found"
                
    def index(self, item):
        x = self.head
        y = 0
        while x != None:
            if x.value == item:
                return y
            else:
                y += 1
            x = x.next
        return "-1"

    def size(self):
        return self.sizee

    def pop(self, pos):
        if self.head == None:
            return "Out of Range"
        x = self.head
        if pos == 0:
            self.head = x.next
            x = None
            self.sizee -= 1
            return "Success"
        for i in range(pos-1):
            x = x.next
            if x is None:
                break
        if x is None:
            return "Out of Range"
        if x.next is None:
            return "Out of Range"
        next = x.next.next

        x.next = None
        x.next = next
        return "Success"


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)