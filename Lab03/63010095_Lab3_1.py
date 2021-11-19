class Stack():
    def __init__(self, ls = None):
        if ls == None:
            self.items = []
        else:
            self.items = list     

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

s = Stack()
input = input("Enter Input : ").replace(","," ").split()
x = 0
while x < len(input):
    if input[x] == "A":
        s.push(input[x+1])
        print(f"Add = {input[x+1]} and Size = {s.size()}")
        x += 2
    else:
        if not s.isEmpty():
            print(f"Pop = {s.pop()} and Index = {s.size()}")
        else:
            print("-1")
        x += 1
if s.isEmpty():
    print("Value in Stack = Empty")
else:
    print("Value in Stack = ",end="")
    for i in s.items:
        print(i,end=" ")