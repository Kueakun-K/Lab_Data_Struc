class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,msize):
        self.head = None
        self.msize = int(msize)
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "[]"
        cur, s = self.head, "["
    
        while cur.next != None:
            s += str(cur.data) + ", "
            cur = cur.next
        
        s += str(cur.data) + "]"
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
        self.size += 1

    def arrive(self, item):
        p = Node(item)
        check = False
        t = self.head
        while t.next != None:
            if t.data == item:
                check = True
                break
            else:
                t = t.next
        if self.msize > self.size and check == False:
            if self.head == None:
                self.head = p
            else:
                t = self.head
                while t.next != None:
                    t = t.next
                t.next = p
            self.size += 1
            return "arrive"
        elif check == True:
            return "already"
        elif self.msize <= self.size:
            return "cannot"
        
    def depart(self,index):
        t = self.head
        check = False
        while t.next != None:
            if t.data == index:
                check = True
                break
            else:
                t = t.next
        t = self.head
        if check == True:
            if t.data == index:
                self.head = t.next
            else:
                while t:
                    if t.data == index:
                        break
                    else:
                        x = t
                        t = t.next
                x.next = t.next
                t = None
            return "depart"
        else:
            return "cannot"


print("******** Parking Lot ********")
input = input("Enter max of car,car in soi,operation : ").split()
x = int(input[0])
L = LinkedList(x)

if input[1] != "0" :
    app = input[1].split(",")
    for i in app:
        L.append(i)

if input[2] == "arrive":
    if input[1] == "0":
        L.append(input[3])
        print(f"car {input[3]} arrive! : Add Car {input[3]}")
    else:
        x = L.arrive(input[3])
        if x == "arrive":
            print(f"car {input[3]} arrive! : Add Car {input[3]}")
        elif x == "already":
            print(f"car {input[3]} already in soi")
        else:
            print(f"car {input[3]} cannot arrive : Soi Full")
elif input[2] == "depart":
    if input[1] != "0":
        y = L.depart(input[3])
    if input[1] == "0":
        print(f"car {input[3]} cannot depart : Soi Empty")
    elif y == "depart":
        print(f"car {input[3]} depart ! : Car {input[3]} was remove")
    elif y == "cannot":
        print(f"car {input[3]} cannot depart : Dont Have Car {input[3]}")

print(L)