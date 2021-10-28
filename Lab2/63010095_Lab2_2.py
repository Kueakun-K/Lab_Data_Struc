import math
class Spherical:

    def __init__(self,r):

        self.radius = r 

    def changeR(self,Radius):

        self.radius = Radius

    def findVolume(self):

        return (4/3)*math.pi*self.radius**3

    def findArea(self):

        return 4*math.pi*self.radius**2

    def __str__(self):

        return f"Radius ={self.radius}"

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1,"Volumn =",R1.findVolume(),"Area =",R1.findArea())
R1.changeR(int(r2))
print(R1,"Volumn =",R1.findVolume(),"Area =",R1.findArea())
