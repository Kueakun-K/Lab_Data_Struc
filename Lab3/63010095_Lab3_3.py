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

def postFixeval(st):

    s = Stack()

    for i in st:
        if i == "+":
            s.push(s.pop()+s.pop())
        elif i == "-":
            o1 = s.pop()
            o2 = s.pop()
            s.push(o2-o1)
        elif i == "*":
            s.push(s.pop()*s.pop())
        elif i == "/":
            o1 = s.pop()
            o2 = s.pop()
            s.push(o2/o1)
        else:
            s.push(int(i))

    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())

print("Answer : ",'{:.2f}'.format(postFixeval(token)))

