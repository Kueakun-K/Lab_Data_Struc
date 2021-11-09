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
            self.printTree(self.root)
            print("--------------------------------------------------")
        else:
            p = self.root
            while True:
                newData = Node(data)
                if data > p.data:  
                    if p.right is None:
                        p.right = newData
                        self.printTree(self.root)
                        print("--------------------------------------------------")
                        break 
                    p = p.right 
                else:
                    if p.left is None:
                        p.left = newData
                        self.printTree(self.root)
                        print("--------------------------------------------------")
                        break 
                    p = p.left 
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)  

def closestValue(root,value):
    gap = 99999999999
    close = 0
    while root is not None:
        if abs(root.data - value) < gap:
            gap = abs(root.data - value)
            close = root.data
        if value == root.data:
            break
        elif value < root.data:
            root = root.left
        else:
            root = root.right
    return close
         

T = BST()
input = input('Enter Input : ').split("/")
inp = [int(i) for i in input[0].split()]
for j in inp:
    root = T.insert(j)

print(f"Closest value of {input[1]} : {closestValue(root,int(input[1]))}")