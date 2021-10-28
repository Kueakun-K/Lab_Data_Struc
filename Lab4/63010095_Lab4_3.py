class Queue():
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list   

    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmptry(self):
        return self.items == []

    def size(self):
        return len(self.items)

code = Queue()
secret = Queue()

input , hint= input("Enter code,hint : ").split(",")
check = ord(hint) - ord(input[0])
for i in input:
    code.enQueue(i)

while not code.isEmptry(): 
    x = ord(code.deQueue()) 
    ed = chr(x+check)
    secret.enQueue(ed)
    print(secret.items)

