class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,size,maxcolli):
        self.size = size
        self.maxcolli = maxcolli
        self.table = []
        for i in range(size):
            self.table.append(None)

    def __str__(self):
        d = ""
        for i in range(len(self.table)):
            d = d+"#"+str(i+1)+"      "+str(self.table[i])+"\n"
        return d

    def insert(self,key,value):
        originalkeysum = 0
        for i in key:
            originalkeysum += ord(i)
        collicheck = 0
        keysum = originalkeysum
        while True:
            if collicheck == self.maxcolli:
                print("Max of collisionChain")
                break
            elif self.table[keysum%self.size] is not None:
                collicheck += 1
                print(f"collision number {collicheck} at {keysum%self.size}")
                keysum =originalkeysum + (collicheck*collicheck)
            else:
                self.table[keysum%self.size] = Data(key,value)
                break

    def isFull(self):
        c=0
        for i in self.table:
            if i is not None:
                c+=1
        return c==self.size


print(" ***** Fun with hashing *****")
input = input("Enter Input : ").split("/")
inp = [int(i) for i in input[0].split()]
H = hash(inp[0],inp[1])
data = input[1].split(",")
for j in range(len(data)):
    if (H.isFull()):
        print("This table is full !!!!!!")
        break
    tmp = data[j].split()
    H.insert(tmp[0],tmp[1])
    print(H,end="")
    print("---------------------------")
