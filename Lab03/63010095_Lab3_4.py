class Stack():
    def __init__(self, ls = None):
        if ls == None:
            self.items = []
        else:
            self.items = list()     

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

def infix2postfix(exp) :

    s = Stack()
    postfix = ""
    # print(s.items)
    
    for i in exp:
        # print(s.items , postfix)
        if i.isalpha() == True:
            postfix += i
        elif i == "(":
            s.push(i)
        elif i == ")":          
            while s.peek() != "(":
                postfix += s.pop() 
            s.pop()
        elif i in ("+-*/"):
            if s.isEmpty():
                s.push(i)
            else:
                if (i in ("*","/") and s.peek() in ("+","-") )or s.peek() == "(":
                    s.push(i)
                else:
                    if i in ("+-"):
                        while s.peek() != "(" :
                            postfix += s.pop()
                            if s.isEmpty():
                                break
                    else:
                        while s.peek() not in ("(+-") :
                            postfix += s.pop()
                            if s.isEmpty():
                                break
                    s.push(i)


    while not s.isEmpty():
        postfix += s.pop()


    return postfix
        

print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

print(infix2postfix(token))
























