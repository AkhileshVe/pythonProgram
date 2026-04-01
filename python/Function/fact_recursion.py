# def fact(x):
#     # print(x)
#     if(x == 1):
#         f = 1
#     else:
#         f=x*fact(x-1)
#     return f
# res = fact(5)
# print("fact = ",res)

# natural number sum using recursion
# input digit sum using recursion
# print the fibonacci seris using recursion

# def natural(x):
#     print(x)
#     if(x==1):
#         f=1
#     else:
#         f = x+natural(x-1)
#     return f

# result = natural(5)
# print(result)


# print the fibonacci seris using recursion (0,1,1,2,3,5,8,13,21)








# dusra tarika fabinachi
# def fib(x ,n1=0, n2=1):
#     if x > 0:
#         print(n1)
#         fib(x-1,n2,n1+n2)

# fib(8)
     

# find the palandrome number

# i = 1
# n = int(input("enter any number : ")) #5268
# sum = 0
# rev = 0
# m = n
# result = ""
# while n>0:

    # r = n % 10
    # n = n // 10
    # rev = rev *10 +r
    # i += 1

#     r = n % 10
#     n = n // 10
#     rev = rev*10  + r 

#     if(rev==m):
#         result = "it is a palandrome"
#     else:
#         result = "it is not a palandrome"

# print(result)

a = 0
b = 1
for x in range(1,8):
    print(a)
    c = a+b
    a = b 
    b = c


     