
class Node:
    def __init__(self, data,index):
        self.data = data
        self.index = index
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data,index):
        if self.root is None:
            self.root = Node(data,index)
        else:
            p = self.root
            while True:
                newData = Node(data,index)
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

    def sumpower(self,root):
        if root.right is None and root.left is None:
            return root.data
        elif root.right is None:
            return self.sumpower(root.left) + root.data
        elif root.left is None:
            return self.sumpower(root.right) + root.data
        else:
            return self.sumpower(root.right) + self.sumpower(root.left) + root.data

    def search(self,root,index):
        if root.right is None and root.left is None:
            if root.index == index:
                return root.data
            else:
                return 0
        elif root.right is None:
            if root.index == index:
                return root.data
            else:
                return self.search(root.left,index)
        elif root.left is None:
            if root.index == index:
                return root.data
            else:
                return self.search(root.right,index)
        else:
            if root.index == index:
                return root.data
            else:
                return self.search(root.right,index) + self.search(root.left,index)

    def compare(self,index1,index2,max):
        sum1 = self.search(self.root,index1)
        sum2 = self.search(self.root,index2)
        for i in range(max):
            if i == (2*index1)+1 or i == (2*index1)+2:
                sum1 += self.search(self.root,i) 
        for j in range(max): 
            if j == (2*index2)+1 or j == (2*index2)+2:
                sum2 += self.search(self.root,j)
        if sum1 == sum2:
            return f"{index1}={index2}"
        elif sum1 < sum2:
            return f"{index1}<{index2}"
        else:
            return f"{index1}>{index2}"

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)  

T = BST()
input = input('Enter Input : ').split("/")

inp = [int(i) for i in input[0].split()]
for j in range(len(inp)):
    root = T.insert(inp[j],j)

cp = input[1].replace(","," ").split()
cp = [int(k) for k in cp]
print(T.sumpower(root))
x = 0
while x < len(cp):
    print(T.compare(cp[x],cp[x+1],len(inp)))
    x += 2

# T.printTree(root)
# print(T.compare(0,2,len(inp)))
