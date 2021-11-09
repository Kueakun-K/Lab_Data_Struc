class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            print("*")
            self.root = Node(data)
        else:
            p = self.root
            while True:
                newData = Node(data)
                if data > p.data:  
                    print("R",end="")
                    if p.right is None:
                        p.right = newData
                        print("*")
                        break 
                    p = p.right 
                else:
                    print("L",end="")
                    if p.left is None:
                        p.left = newData
                        print("*")
                        break 
                    p = p.left 
        return self.root

T = BST()
input = [int(i) for i in input('Enter Input : ').split()]
for i in input:
    root = T.insert(i)