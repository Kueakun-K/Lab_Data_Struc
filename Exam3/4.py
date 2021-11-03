class TreeNode(object):

    def __init__(self, x):

        self.val = x

        self.left = None

        self.right = None



def list_to_bst(list_nums):
    num = int(len(list_nums)/2)
    node = TreeNode(list_nums.pop(num))
    x = node
    while len(list_nums) != 0:
        i = int(len(list_nums)/2)
        j = list_nums.pop(i)
        node = x
        newdata = TreeNode(j)
        while True:
            if j < node.val:
                if node.left is None:
                    node.left = newdata
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = newdata
                    break
                else:
                    node = node.right
    node = x
    return node



def preOrder(node): 

    if not node: 

        return      

    print(node.val)

    preOrder(node.left) 

    preOrder(node.right)   



def printBST(node,level = 0):

    if node != None:

        printBST(node.right, level + 1)

        print('     ' * level, node.val)

        printBST(node.left, level + 1)



list_nums = sorted([int(item) for item in input("Enter list : ").split()])

result = list_to_bst(list_nums)




print("\nList to a height balanced BST : ")

print(preOrder(result))

print("\nBST model : ")

printBST(result)