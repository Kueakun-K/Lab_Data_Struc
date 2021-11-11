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
               
    def below(self,root,check):
        if root != None:
            self.below(root.left,check)
            if root.data<check:
                print(root.data,end=" ")
            self.below(root.right,check)

    def checkHaveBelow(self,root,check):
        if root.left != None:
            return self.checkHaveBelow(root.left,check)
        else:
            return root.data < check

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    

T = BST()
inp,num = input("Enter Input : ").split('|')
inp = inp.split()
for i in range(len(inp)):
    data = int(inp[i])
    root = T.insert(data)
T.printTree(root)
print("--------------------------------------------------")
print(f"Below {num} : ",end="")
if not T.checkHaveBelow(root,int(num)):
    print("Not have")
T.below(root,int(num))

