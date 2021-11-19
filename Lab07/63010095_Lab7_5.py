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
            self.root = Node(data)
        else:
            p = self.root
            while True:
                newData = Node(data)
                if data > p.data:  
                    if p.right is None:
                        p.right = newData
                        break 
                    p = p.right 
                else:
                    if p.left is None:
                        p.left = newData
                        break 
                    p = p.left 
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self, data,node):
        if data==self.root.data:
            print("Root")
            return
        if node.data==data:
            if node.left !=None or node.right != None:
                print("Inner")
                return
            else :
                print("Leaf")
                return
        elif node.data>data:
            if node.left!= None:
                self.checkpos(data,node.left)
            else:
                print("Not exist")
                return
        elif node.data<data:
            if node.right!= None:
                self.checkpos(data,node.right)
            else:
                print("Not exist")
                return

 
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0],root)