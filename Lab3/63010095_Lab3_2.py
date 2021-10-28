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

def match(open, close):
    return (open == '(' and close == ')') or \
            (open == '{' and close == '}') or \
            (open == '[' and close == ']')

input = input("Enter expresion : ")
s = Stack()
i = 0
error = 0
while i < len(input) and error == 0:
    x = input[i]
    if x in "({[":
        s.push(x)
    else:
        if x in ")}]":
            if s.size() > 0:
                if not match(s.pop(),x):
                    error = 1
            else:
                error = 2
    i += 1

if s.size() > 0 and error == 0:
    error = 3

if error == 1:
    print(f"{input} Unmatch open-close")
elif error == 2:
    print(f"{input} close paren excess")
elif error == 3:
    print(f"{input} open paren excess   {s.size()} : ",end="")
    for y in s.items:
        print(y,end="")
else:
    print(f"{input} MATCH")