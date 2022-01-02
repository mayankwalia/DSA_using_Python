class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def is_valid(self):
        if (self.a+self.b>self.c) and (self.a+self.c>self.b) and (self.b+self.c>self.a):
            return 'Valid'
        else:
            return 'Invalid'
        
    def Side_Classification(self):
        if self.is_valid()=='Valid':
            if (self.a==self.b and self.b==self.c):
                return 'Equilateral'
            elif (self.a==self.b or self.b==self.c or self.a==self.c):
                return 'Isosceles'
            else:
                return 'Scalene'
        else:
            return 'Invalid'
    def Angle_Classification(self):
        if self.is_valid()=='Valid':
            l=sorted([self.a,self.b,self.c])
            a,b,c=l
            if ((a)**2+(b)**2 >(c)**2):
                return 'Acute'
            elif  ((a)**2+(b)**2 ==(c)**2):
                return 'Right'
            else:
                return 'Obtuse'
        else:
            return 'Invalid' 
    def Area(self):
        if self.is_valid()=='Valid':
            a,b,c=[self.a,self.b,self.c]
            s=(a+b+c)/2
            area=(s*(s-a)*(s-b)*(s-c))**0.5
            return area
        else:
            return 'Invalid'    
a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())
