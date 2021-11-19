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
    
    def preoder(self,root):
        if root is not None:
                print(root.data,end=' ')
                self.preoder(root.left)
                self.preoder(root.right)

    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)
    
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=' ')
    
    def postorder1(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=' ')
    
    def breadth(self,root):
        if root is None:
            return
        queue = [root]
        data = []
        while len(queue)!= 0:
            node = queue.pop(0)
            data.append(node.data)
            if(node.left):
                 queue.append(node.left)
            if(node.right):
                 queue.append(node.right)
                 
        for i in data:
            print(i,end=" ")
        
                
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node) 
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

print("Preorder : ",end='')
T.preoder(root)
print()
print("Inorder : ",end='')
T.inorder(root)
print()
print("Postorder : ",end='')
T.postorder(root)
print()
print("Breadth : ",end='')
T.breadth(root)