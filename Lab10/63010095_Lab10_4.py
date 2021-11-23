class Rehashing:
    def __init__(self,size,MaxCollision,Threshold):
        self.size = size
        self.maxcoll = MaxCollision
        self.maxthreshold = Threshold
        self.table = []
        self.datatemp = []
        self.count = 0
        for i in range(size):
            self.table.append(None)

    def __str__(self):
        s = ""
        for i in range(len(self.table)):
            s += "#"+str(i+1)+"\t"+str(self.table[i])+"\n"
        return s

    def thresholdCheck(self,data):
        if float(self.count+1)/float(self.size)*100>self.maxthreshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()

    def insert(self,data,isrehash=False):
        self.thresholdCheck(data)
        collicheck = 0
        tmp = data % self.size
        while self.table[tmp] is not None:
            collicheck += 1
            print(f"collision number {collicheck} at {tmp}")
            if collicheck == self.maxcoll:
                if isrehash == False:
                    print("****** Max collision - Rehash !!! ******")
                self.rehash()
                collicheck = 0
            tmp = data + (collicheck * collicheck)
            tmp = tmp % self.size
        self.table[tmp] = data 
        if isrehash == False:
            self.datatemp.append(data)
            self.count += 1

    def rehash(self):
        self.size = self.size * 2
        while not self.isPrime(self.size):
            self.size += 1
        self.table = []
        for i in range(self.size):
            self.table.append(None)
        for j in self.datatemp:
            self.insert(j,True)

    def isPrime(self,num):
        for i in range(num-2):
            if num%(i+2)==0:
                return False
        return True  

print(" ***** Rehashing *****")
input = input("Enter Input : ").split("/")
inp = [int(i) for i in input[0].split()]
data = [int(j) for j in input[1].split()]
RH = Rehashing(inp[0],inp[1],inp[2])
print("Initial Table :")
print(RH,end="")
print("----------------------------------------")
for k in data:
    print(f"Add : {k}")
    RH.insert(k)
    print(RH,end="")
    print("----------------------------------------")