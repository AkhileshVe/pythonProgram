class Time:
    def __init__(self,h=0,m=0,s=0):
        self.h = h
        self.m = m
        self.s = s

    def display(self):
        print("hour : ",self.h, end=" ")
        print("hour : ",self.m, end=" ")
        print("hour : ",self.s, end=" ")
    
    def addTime(self,k1,k2):
        self.h = k1.h+k2.h
        self.m = k1.m+k2.m
        self.s = k1.s+k2.s

        if self.s >= 60:
            self.m = self.m+self.s//60
            self.s = self.s % 60
        
        if( self.m >= 60):
            self.h = self.h+self.m//60
            self.m = self.m % 60 


t1 = Time(2,45,55)
t2 = Time(3,50,55)
t3 = Time()

t1.display()
print()
t2.display()
print()
t3.addTime(t1,t2)

t3.display()