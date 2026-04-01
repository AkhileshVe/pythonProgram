# class Area:

#     def __init__(self,l=0, b=0):
#         self.l = l
#         self.b = b

#     def a(self):
#         return self.l* self.b

# ob = Area(6,5)
# print("Area = ", ob.a())


# ================================= single inheriance


# class Area:

#     def __init__(self,l=0, b=0):
#         self.l = l
#         self.b = b

#     def a(self):
#         return self.l* self.b
    
# class Volume(Area):
#     def __init__(self,l=0, b=0 , h=0):
#         # Area.__init__(self,l,b)
#         super().__init__(l,b)
#         self.h = h
#     def v(self):
#         return self.a() * self.h

# ob = Volume(6,5,3)
# print("Area = ", ob.a())
# print("Volume = ", ob.v())




# ================================= multilavel  inheritance=====

# class Area:

#     def __init__(self,l=0, b=0):
#         self.l = l
#         self.b = b

#     def a(self):
#         return self.l* self.b
    
# class Volume(Area):
#     def __init__(self,l=0, b=0 , h=0):
#         # Area.__init__(self,l,b)
#         super().__init__(l,b)
#         self.h = h
#     def v(self):
#         return self.a() * self.h
    
# class Density(Volume):
#     def __init__(self,l=0, b=0 , h=0, m=0):
#         # Volume.__init__(self,l,b)
#         super().__init__(l,b,h)
#         self.m = m
#     def d(self):
#         return self.m/self.v()

# ob = Density(6,5,3,217.45)
# print("Area = ", ob.a())
# print("Volume = ", ob.v())
# print("density = ", ob.d())





# ================================= multipal inheritance

# class 1
# class Square:
#     def __init__(self,h=0):
#         self.h = h

#     def sq(self):
#         return self.h * self.h

# # class 2
# class Area:

#     def __init__(self,l=0, b=0):
#         self.l = l
#         self.b = b

#     def a(self):
#         return self.l* self.b

# # class 3
# class Volume(Area, Square):

#     def __init__(self,l=0, b=0 , h=0):
#         Area.__init__(self,l,b)
#         Square.__init__(self,h)
#     def v(self):
#         return self.a() * self.h
    

# ob = Volume(6,5,3)
# print("Area = ", ob.a())
# print("Squere = ", ob.sq())
# print("Volume = ", ob.v())

# # ob2 = 
# print(Square(4).sq())



# ================================= h inheritance


# class Student:
#     def __init__(self,roll_no = 0 , name=""):
#         self.roll_no = roll_no
#         self.name = name
    
#     def diaplay(self):
#         print("roll no : ",self.roll_no)
#         print("Name: ",self.name)


# class Extra:
#     def __init__(self,sport = 0 , mis=""):
#         self.sport = sport
#         self.mis = mis
    
#     def diaplay(self):
#         print("sport no : ",self.sport)
#         print("mis no: ",self.mis)


# class Marks(Student):
#     def __init__(self,roll_no = 0 ,name = "", p=0,c=0,m=0):
#         super().__init__(roll_no,name)
#         self.p = p
#         self.c = c
#         self.m = m
    
#     def diaplay(self):
#         super().diaplay
#         print("physics no : ",self.p)
#         print("chamistry no: ",self.c)
#         print("maths no: ",self.m)

# class Result(Marks,Extra):
#     def __init__(self,roll_no = 0 ,name = "", p=0,c=0,m=0,sport=0,mis=0):
#         Marks.__init__(self,roll_no,name,p,c,m)
#         Extra.__init__(self,sport,mis)    
#     def diaplay(self):
#         Marks.diaplay(self)
#         Extra.diaplay(self)
#     def total(self):
#         total =self.p+self.c+self.m+self.sport+self.mis
#         return total
#     def percentage(self,total):
#         per = total/5
#         return per

# res = Result(1,"Akhil",89,78,98,99,78)
# res.diaplay()
# tot = res.total()
# per = res.percentage(tot)
# print("total : ", tot)
# print("percentage : ", per)








# ======================================== herachichal 
# from abc import abstractmethod,ABC
# class Test(ABC): 
#     def __init__(self,x=0):
#         self.x=x
    
#     @abstractmethod
#     def display(self):
#         pass


# class 1
class Test: 
    def __init__(self,x=0):
        self.x=x

    def display(self):
         print("X = ",self.x,)

# class 2
class Test2(Test):
    def __init__(self, x=0,y=0):
        super().__init__(x)
        self.y=y
    def display(self):
        print("X = ",self.x, end=" ")
        print("Y = ",self.y)

# class 3
class Test3(Test2):
    def __init__(self, x=0,y=0,z=0):
        Test2.__init__(self,x,y)
        self.z=z
    def display(self):
        print("X = ",self.x, end=" ")
        print("Z = ",self.z)

t1 = Test2(25)
t2 = Test3(45)


t1.display()
print("===========================")
t2.display()
print("===========================")