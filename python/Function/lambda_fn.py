# # A lambda function is a small anonymous function defined using the lambda keyword that 
# # can take any number of arguments but only one expression.

# add = lambda x,y : x+y
ob1 = lambda x,y : x if x > y else y
print(ob1(4,40))


# # ++++++++++++++++++++  Inner lambda 
# add = lambda x: lambda y: lambda z: x+y+z

# res1 = add(20)(10)(12)
# print(res1)


# # Anonymous Object example
# # ++++++++++++++++++++  
# def add(x):
#     def addTwo(y):
#         return x+y
#     return addTwo

# ob = add(7)
# res = ob(8)

# print(res)

# # ++++++++++++++++++++  
# # ++++++++++++++++++++  
def add(x):
    def addTwo(y):
        def addThree(z):
            return x+y+z
        return addThree
    return addTwo

res = add(8)(15)(7)
print(res)

# ++++++++++++++++++++  
    

# ls = [1,2,3,4,5,6,7,8]
# print(ls)

# res = list(filter(lambda x: x% 2 == 0 , ls))
# res = set(filter(lambda x: x% 2 == 0 , ls))

# res = list(filter( lambda x : x % 2 != 0 , ls))
# res1 = list(filter( lambda x : x % 2 == 0 , ls))

# print("odd number",res )
# print("Even number",res1)



# Map using lambda

ls = [1,2,3,4,5,6,7,8,9]

squ = list(map(lambda x: x**2 ,ls))
print(squ)


friend_ls = ["akhilesh", 'raj', 'rohit', 'abhishek']

length = set(map(lambda x: len(x) ,friend_ls))
print(length)