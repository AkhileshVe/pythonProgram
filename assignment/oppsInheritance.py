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
class Square:
    def __init__(self,h=0):
        self.h = h

    def sq(self):
        return self.h * self.h

# class 2
class Area:

    def __init__(self,l=0, b=0):
        self.l = l
        self.b = b

    def a(self):
        return self.l* self.b

# class 3
class Volume(Area, Square):

    def __init__(self,l=0, b=0 , h=0):
        # Area.__init__(self,l,b)
        # Square.__init__(self,h)
        super().__init__(l,h)
        # self.l = l
        # self.b = b
        self.h = h
    def v(self):
        return self.a() * self.h
    

ob = Volume(6,5,3)
print("Area = ", ob.a())
print("Squere = ", ob.sq())
print("Volume = ", ob.v())

# ob2 = 
# print(Square(4).sq())