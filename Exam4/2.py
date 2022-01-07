class Node:
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class AVL:
    
    def insert(self, root, key):    
        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getheight(root.left),self.getheight(root.right))
       
        b = self.getBalance(root)
        if b> 1 and key >= root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if b < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        if b > 1 and key < root.left.data:
            return self.rightRotate(root)

        if b < -1 and key >= root.right.data:
            return self.leftRotate(root)
        return root
 
    def leftRotate(self, z):
 
        y = z.right

        T2 = y.left
 
        y.left = z
        z.right = T2
 
        z.height = 1 + max(self.getheight(z.left),self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left),self.getheight(y.right))
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getheight(z.left),self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left),self.getheight(y.right))

        return y

    def getheight(self, root):
        if not root:
            return 0
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
        return self.getheight(root.left) - self.getheight(root.right)
     
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data,"",end='')
            self.inorder(root.right)

    def preoder(self,root):
        if root is not None:
            print(root.data,"",end='')
            self.preoder(root.left)
            self.preoder(root.right)
    
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,"",end='')
    

T = AVL()
root = None
print(" *** AVL Tree ***")
input = [int(i) for i in input('Enter some numbers : ').split()]
for i in input:
    root = T.insert(root,i)
print("in_order  --> ",end='')
T.inorder(root)
print()
print("preorder  --> ",end='')
T.preoder(root)
print()
print("postorder --> ",end='')
T.postorder(root)
print()
