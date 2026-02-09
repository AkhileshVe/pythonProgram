# def display():
#     print("hello display")

# # display()


# def addition(a,b,c):
#     add = a + b
#     print(add)
#     c()
    

# addition(4,5, display)

# def add(a, b):
#      print( a + b)

# add(7, 3)


# with return , without argument

# def factorial():
#     n = int(input("Enter any number for factorial : "))
#     i = 1
#     fact = 1

#     while i <= n:
#         fact *= i 
#         i+=1
#     return fact


# result = factorial()
# print("fact",result+5)


# with return , without argument
 
# def factorial():
#     n = int(input("Enter any number for factorial : "))
#     i = 1
#     fact = 1

#     while i <= n:
#         fact *= i 
#         i+=1
#     print( fact)


# factorial()



# find the four greatest number
# No return type with argument

# def greatest(a,b,c,d):
#     if(a>b and a>c and a>d):
#         print(a ," is grratest")
#     elif(b>a and b>c and b>d):
#         print(b ," is grratest")
#     elif(c>b and c>a and c>d):
#         print(c ," is grratest")
#     elif(d>b and d>c and d>a):
#         print(d ," is grratest")


# a=int(input("Enter first number : "))
# b=int(input("Enter second number : "))
# c=int(input("Enter third number : "))
# d= int(input("Enter forth number : "))

# greatest(a,b,c,d)


def check_Primre(x):
    i = 2
    flag =1
    while i < x and flag == 1:
        if(x % i==0):
            flag = 0
        i += 1
    return flag 

n = int(input("Enter a number : "))

res = check_Primre(n)

if(res == 1):
    print("Prime number.......")
else:
    print("Not prime number ......")