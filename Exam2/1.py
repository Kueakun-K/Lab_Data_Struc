class Stack():
    def __init__(self,ls = None):
        if ls == None:
            self.item = []
        else:
            self.item = list()

    def __str__(self):
        return str(self.item)

    def push(self,data):
        self.item.append(data)

    def pop(self):
        self.item.pop()

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def peek(self):
        return self.item[-1]

    def bottom(self):
        return self.item[0]
        
s1 = Stack()
input = int(input("Enter choice : "))

if input == 1:
    s1.push(10)
    s1.push(20)
    print("Data in Stack is : ",end="")
    for i in s1.item:
        print(i,end=" ")
    print()
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())

elif input == 2:
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print("Data in Stack is : ",end="")
    for i in s1.item:
        print(i,end=" ")
    print()
    print("Stack is Empty :",s1.isEmpty())

elif input == 3:
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print("Data in Stack is : ",end="")
    for i in s1.item:
        print(i,end=" ")
    print()
    print("Stack size :",s1.size())